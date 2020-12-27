class Representable:
    def __repr__(self):
        literal = [f'{key}:{value}' for key, value in vars(self).items()]
        return f'<{", ".join(literal)}>'
