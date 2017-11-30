from durable.lang import *

with ruleset('replacetoken'):
    # antecedent
    @when_all(count(1), m.word.imatches(".*today.*"))
    def match_today(c):
        c.s.replace_str = "today"
        c.s.replace_with = datetime.datetime.now().strftime('%d:%m:%Y')
        # consequent
        print('Hello {0}'.format(c.m.word))

    @when_all(+m.paragraph)
    def replace_op(c):
        print('Hello {0}'.format(c.m.paragraph))

    # on ruleset start
    @when_start
    def start(host):    
        host.post('replacetoken', { 'word': 'world', 'paragraph':'Hello world in rules', })

run_all()

