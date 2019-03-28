# Interpy: internationalization made _easy_.

你好，世界！

Like music and natural languages, programming is a lot easier to learn when
you're young. The problem is that seven-year-olds have the attention span of
seven-year-olds, and it's a little silly to expect them to simultaneously learn
English just so they can use their computer. The mental effort of constantly
parsing a natural language you don't speak on top of the effort of parsing a
new programming language makes learning harder than it needs to be, and takes
you out of the flow of programming.

Interpy tries to solve this problem by providing a set of bindings for Python
keywords and common built-in functions in a few non-English natural languages,
and a dead-simple preprocessor to translate them. The Interpy user experience
should feel like programming in _your_ native language, frictionlessly.

## Installation
Currently, there isn't any nice installation procedure set up. If you're
working on a unix system like Linux, BSD or MacOS, I recommend cloning this
repository and simply symlinking the top-level script:
    $ ln -s /path/to/interpy.py /usr/bin/interpy
Of course, take care when you're doing anything like this, even if it looks
harmless!
In the future, I hope to add a better/less manual installation process.

## Usage
Interpy almost purely extends the python interpreter already on your machine.
You can use it like this:
    $ interpy bonjour.py
    bonjour le monde!
    $
How does Interpy know what language to use? It tries three things, in order:
1. Look for a command-line flag like `--fr`.
2. Look for a helpful  annotation like `# lang=fr` near the top of
   `bonjour.py`.
3. (Crudely) count keywords matching those from any of the supported languages,
   and try to infer the intended language.

Furthermore, in a future version, you will be able to use Interpy like this:
    $ interpy --fr
    >>> si Vrai:
    ...     imprime('bonjour le monde!')
    ...
    bonjour le monde!
    >>>

You will also be able to use  it to "compile" localized code to ordinary Python
like this:
    $ interpy -o my_script.py mon_script.py
    $ ls
    my_script.py    mon_script.py
Note that, despite the suggestive notation, the output here _isn't_ object code
that your machine knows what to do with. You still need to run it through a
Python interpreter!

Alors, bon chance et joyeux hacking!

## Questions

### What languages are currently supported?
We currently have bindings for French, standard German, Russian, and Simplified
Chinese. Right now, they're all incomplete, but you can write some simple
programs using the occasional English-named function as needed.

### Why don't you support Xhosa or Estonian?
There's no reason we can't! Feel free to fork this project and/or submit a pull
request.

### Can you handle character set X?
The Python interpreter--and Interpy--expects UTF-8-encoded input, so you can
use any unicode characters you like. See the Russian and Simplified Chinese
examples in `examples/privyet.py` and `examples/nihao.py`. I don't have  RtL
languges yet, but it won't be too hard. In a future release I'll probably add
support for Arabic/Farsi/Hebrew.

### Isn't this problem solved by \_\_\_\_\_\_?
Sure, probably. I didn't do any research before writing this.

### Is this actually a better way to learn how to program?
I have no idea. For all I know, it might just be counterproductive.

### Is there any overhead when using Interpy?
Yes. This is partly because the implementation is
simple-bordering-on-braindead, and partly inevitable. The overhead should be
linear in the input size, though, so it's (asymptotically) as good as can be,
and in practice isn't noticeable on little scripts. Furthermore, Interpy can be
used to "compile" localized code to ordinary Python, which then runs without
overhead.

### The connotation of one of the words in your Russian mapping is hilariously wrong!
That's not a question, but the answer is: please let me know! Feel free to make
pull requests with this kind of correction. I 200% expect there to be errors of
this sort.

### How do you handle highly-inflected languages?
Mostly by ignoring the obvious problems. I've tried to keep verb-named
functions in the (familiar) imperative, since you're telling the computer to
"do this thing." I'm sure that I've gotten this convention wrong in at least a
few places.

### Why are the bindings incomplete?
I'm working on improving coverage, but there are a few things that tend to make
this challenging.
* Python has a lot of built-in functions.
* I bit off more than I could chew by starting with four languages.
* I don't really speak these languages, so the more bindings I add, the more
  likely it becomes that many of them are awkward or dead wrong.
* Some Python keywords are common English words that have no exact analogue in
  the target language(s) because of fundamental grammatical differences.
Again, feel free to help out by making pull requests! I will probably blindly
trust your grasp of language X.

### Does this work with python 2?
No, but not for any important reason. If anyone wants python 2 support, I can
add it.
