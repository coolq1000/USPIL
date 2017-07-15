# USPIL
The Ultra Simple Python Interpreted Language

#### _Note_
_`This language is very expiremental! I've only been developing it for a day or two.`_

### Usage
```
python main.py <filename>
```

### Fetures
 * Pure-Python implementation
 * Flexible(ish)
 * Simple
 * Small runtime

### Language
The language itself is very basic, similar to C or JS. It is very simple.

```javascript
var (x = 10)
print(x)
```
`>>> 10`

As you can see, it creates a variable called `x`, then it prints the variable.

```javascript
var (x = 0)
while (x < 10)
{
  print(x)
  var (x = x + 1)
}
```

This will increment `x` until it reaches `10`.

### Require()
Using `require()` we can include other scripts into the current script.

### Comments
You can make comments with `;`.

For example:
```javascript
var (x = 1)
;var (x = 2)
print(x)
```
`>>> 1`

###### Program1.prog
```javascript
require('Program2.prog')
print('Hello from program 1!')
```

###### Program2.prog
```javascript
print('Hello from program 2!')
```

## Todo
|Todo|Done|
|----|----|
|Evaluate expressions without `eval()`|No|
|Switch statement|No|
|For statement|No|
|Allow `var` to work without `(` and `)`|No|
|Implementing arrays|No|

## Information about the files
```
USPIL/ [
  interpreter.py (evaluator)
  lexer.py (makes tokens)
  main.py (this ties it all together)
  parse.py (turns the tokens into something better)
  pre.py (preprocessor, created for `require()`)
]
```

<sub>Readme last updated <15/7/2017> AUS format<sub/>
