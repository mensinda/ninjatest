project('ninjatest', ['cpp'])

res = custom_target('ct', input: ['settings.json'], output: ['test.hpp', 'test.cpp'], command: [find_program('./test.py')])

executable('testPro', ['main.cpp', res[0], res[1]])
