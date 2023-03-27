class FloatUrlConverter:
    # regex = '[0-9]+\.[0-9]+'
    regex = '\d+(?:.|,)?\d'

    def to_python(self, value):
        value = value.replace(',','.')
        return float(value)

    def to_url(self, value):
        return str(value)
