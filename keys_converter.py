from selenium.webdriver.common.keys import Keys


class KeysConverter():
    _keys_map = {
        '9': {'keypad': Keys.NUMPAD9,
              'occurence': None},
        '0': {'keypad': Keys.NUMPAD0,
              'occurence': None},
        '1': {'keypad': Keys.NUMPAD1,
              'occurence': None},
        '2': {'keypad': Keys.NUMPAD2,
              'occurence': None},
        '3': {'keypad': Keys.NUMPAD3,
              'occurence': None},
        '4': {'keypad': Keys.NUMPAD4,
              'occurence': None},
        '5': {'keypad': Keys.NUMPAD5,
              'occurence': None},
        '6': {'keypad': Keys.NUMPAD6,
              'occurence': None},
        '7': {'keypad': Keys.NUMPAD7,
              'occurence': None},
        '8': {'keypad': Keys.NUMPAD8,
              'occurence': None},
        '+': {'keypad': Keys.ADD,
              'occurence': None},
        '-': {'keypad': Keys.SUBTRACT,
              'occurence': None},
        '*': {'keypad': Keys.MULTIPLY,
              'occurence': None},
        '/': {'keypad': Keys.DIVIDE,
              'occurence': None},
        '=': {'keypad': Keys.EQUALS,
              'occurence': None}
    }

    def map_keys(self, element):
        if element in self._keys_map:
            return self._keys_map[element]['keypad']
    
    def update_occurence(self, element: str, occurence: bool, **kwargs):
        if not occurence:
            self._keys_map[element]['occurence'] = False
        else:
            if self._keys_map[element]['occurence'] is None:
                self._keys_map[element]['occurence'] = []
            
                self._keys_map[element]['occurence'].append({
                    'attempted_position': kwargs['position'],
                    'is_correct': kwargs['is_correct']
                })

