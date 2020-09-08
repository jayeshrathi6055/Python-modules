import textwrap

## Use of fill

sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

print(textwrap.fill(sample_text, width=100,initial_indent=" "*4,subsequent_indent=" ",expand_tabs=False,replace_whitespace=True))

## Use of shorten

# print(textwrap.shorten(sample_text,width=50,placeholder="....."))

## Use of dedent

# print(textwrap.dedent(sample_text))

## Use of indent

# print(textwrap.indent(sample_text,">>> "))

##Use of wrap

# a = textwrap.wrap(sample_text,width=70,initial_indent=" "*4,subsequent_indent=" ",expand_tabs=False,replace_whitespace=True)