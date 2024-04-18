import math
import random
from django import template
from PIL import ImageColor

register = template.Library()

class Color:
    def __init__(self, r, g, b):
        self.set(r, g, b)

    def __str__(self):
        return f"rgb({round(self.r)}, {round(self.g)}, {round(self.b)})"

    def set(self, r, g, b):
        self.r = self.clamp(r)
        self.g = self.clamp(g)
        self.b = self.clamp(b)

    def hue_rotate(self, angle=0):
        angle = angle / 180 * 3.141592653589793
        sin = math.sin(angle)
        cos = math.cos(angle)

        self.multiply([
            0.213 + cos * 0.787 - sin * 0.213,
            0.715 - cos * 0.715 - sin * 0.715,
            0.072 - cos * 0.072 + sin * 0.928,
            0.213 - cos * 0.213 + sin * 0.143,
            0.715 + cos * 0.285 + sin * 0.140,
            0.072 - cos * 0.072 - sin * 0.283,
            0.213 - cos * 0.213 - sin * 0.787,
            0.715 - cos * 0.715 + sin * 0.715,
            0.072 + cos * 0.928 + sin * 0.072,
        ])

    def sepia(self, value=1):
        self.multiply([
            0.393 + 0.607 * (1 - value),
            0.769 - 0.769 * (1 - value),
            0.189 - 0.189 * (1 - value),
            0.349 - 0.349 * (1 - value),
            0.686 + 0.314 * (1 - value),
            0.168 - 0.168 * (1 - value),
            0.272 - 0.272 * (1 - value),
            0.534 - 0.534 * (1 - value),
            0.131 + 0.869 * (1 - value),
        ])

    def saturate(self, value=1):
        self.multiply([
            0.213 + 0.787 * value,
            0.715 - 0.715 * value,
            0.072 - 0.072 * value,
            0.213 - 0.213 * value,
            0.715 + 0.285 * value,
            0.072 - 0.072 * value,
            0.213 - 0.213 * value,
            0.715 - 0.715 * value,
            0.072 + 0.928 * value,
        ])

    def multiply(self, matrix):
        new_r = self.clamp(self.r * matrix[0] + self.g * matrix[1] + self.b * matrix[2])
        new_g = self.clamp(self.r * matrix[3] + self.g * matrix[4] + self.b * matrix[5])
        new_b = self.clamp(self.r * matrix[6] + self.g * matrix[7] + self.b * matrix[8])
        self.r = new_r
        self.g = new_g
        self.b = new_b

    def brightness(self, value=1):
        self.linear(value)

    def contrast(self, value=1):
        self.linear(value, -(0.5 * value) + 0.5)

    def linear(self, slope=1, intercept=0):
        self.r = self.clamp(self.r * slope + intercept * 255)
        self.g = self.clamp(self.g * slope + intercept * 255)
        self.b = self.clamp(self.b * slope + intercept * 255)

    def clamp(self, value):
        if value > 255:
            return 255
        elif value < 0:
            return 0
        return value

    def hsl(self):
        r = self.r / 255
        g = self.g / 255
        b = self.b / 255
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin

        l = (cmax + cmin) / 2

        if delta == 0:
            h = 0
            s = 0
        else:
            if cmax == r:
                h = 60 * (((g - b) / delta) % 6)
            elif cmax == g:
                h = 60 * (((b - r) / delta) + 2)
            else:
                h = 60 * (((r - g) / delta) + 4)

            if l < 0.5:
                s = delta / (cmax + cmin)
            else:
                s = delta / (2 - cmax - cmin)

        return {'h': h, 's': s, 'l': l}
    
    def invert(self, value=1):
        self.r = self.clamp((value + self.r / 255 * (1 - 2 * value)) * 255)
        self.g = self.clamp((value + self.g / 255 * (1 - 2 * value)) * 255)
        self.b = self.clamp((value + self.b / 255 * (1 - 2 * value)) * 255)

class Solver:
    def __init__(self, target):
        self.target = target
        self.target_hsl = self.target.hsl()
        self.reused_color = Color(0, 0, 0)

    def solve(self):
        result = self.solve_narrow(self.solve_wide())
        return {
            'values': result['values'],
            'loss': result['loss'],
            'filter': self.css(result['values']),
        }

    def solve_wide(self):
        A = 5
        c = 15
        a = [60, 180, 18000, 600, 1.2, 1.2]

        best = {'loss': float('inf')}
        for i in range(3):
            initial = [50, 20, 3750, 50, 100, 100]
            result = self.spsa(A, a, c, initial, 1000)
            if result['loss'] < best['loss']:
                best = result
        return best

    def solve_narrow(self, wide):
        A = wide['loss']
        c = 2
        A1 = A + 1
        a = [0.25 * A1, 0.25 * A1, A1, 0.25 * A1, 0.2 * A1, 0.2 * A1]
        return self.spsa(A, a, c, wide['values'], 500)

    def spsa(self, A, a, c, values, iters):
        alpha = 1
        gamma = 0.16666666666666666

        best = None
        best_loss = float('inf')
        deltas = [0] * 6
        high_args = [0] * 6
        low_args = [0] * 6

        for k in range(iters):
            ck = c / ((k + 1) ** gamma)
            for i in range(6):
                deltas[i] = 1 if random.random() > 0.5 else -1
                high_args[i] = values[i] + ck * deltas[i]
                low_args[i] = values[i] - ck * deltas[i]

            loss_diff = self.loss(high_args) - self.loss(low_args)
            for i in range(6):
                g = loss_diff / (2 * ck) * deltas[i]
                ak = a[i] / ((A + k + 1) ** alpha)
                values[i] = self.fix(values[i] - ak * g, i)

            loss = self.loss(values)
            if loss < best_loss:
                best = values[:]
                best_loss = loss
        return {'values': best, 'loss': best_loss}

    def fix(self, value, idx):
        max_val = 100
        if idx == 2:
            max_val = 7500
        elif idx in [4, 5]:
            max_val = 200

        if idx == 3:
            if value > max_val:
                value %= max_val
            elif value < 0:
                value = max_val + value % max_val
        elif value < 0:
            value = 0
        elif value > max_val:
            value = max_val
        return value

    def loss(self, filters):
        color = self.reused_color
        color.set(0, 0, 0)

        color.invert(filters[0] / 100)
        color.sepia(filters[1] / 100)
        color.saturate(filters[2] / 100)
        color.hue_rotate(filters[3] * 3.6)
        color.brightness(filters[4] / 100)
        color.contrast(filters[5] / 100)

        color_hsl = color.hsl()
        return (
            abs(color.r - self.target.r) +
            abs(color.g - self.target.g) +
            abs(color.b - self.target.b) +
            abs(color_hsl['h'] - self.target_hsl['h']) +
            abs(color_hsl['s'] - self.target_hsl['s']) +
            abs(color_hsl['l'] - self.target_hsl['l'])
        )

    def css(self, filters):
        def fmt(idx, multiplier=1):
            return round(filters[idx] * multiplier)
        return f"filter: invert({fmt(0)}%) sepia({fmt(1)}%) saturate({fmt(2)}%) hue-rotate({fmt(3, 3.6)}deg) brightness({fmt(4)}%) contrast({fmt(5)}%);"

@register.filter
def to_css_filter(hex_color):
    rgb = hex_to_rgb(hex_color)
    if rgb is None:
        return ""

    color = Color(*rgb)
    solver = Solver(color)
    result = solver.solve()

    return result['filter']

def hex_to_rgb(hex_color):
    try:
        rgb = ImageColor.getcolor(hex_color, "RGB")
        return rgb
    except ValueError:
        return None
