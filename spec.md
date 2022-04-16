# vappy spec

## General
- All programs must start with `Hey guys, did you know that...`
- All programs must end with `Vaporeon is literally built for human dick.`
- `vappy` is newline and tab-agnostic, but we recommend that you use them
for readability.

## Variable assignment
`[variable] can be rough with [expr].`

Example, assigning 10 to `x`:
`x can be rough with 10.` 


## Functions
Function definition:
```
With their abilities [parameters], they can easily [function name] with enough water.
    [function statements]
Vaporeon is literally built for human dick.
```

Example function that multiplies the two parameters together:
```
With their abilities x and y, they can easily multiply with enough water.
    No other Pokemon comes close to this level of x * y.
Vaporeon is literally built for human dick.
```

For a single-parameter function, you can use `ability` in place of `abilities`
to make the grammar work better.

### Return statement
`No other Pokemon comes close to this level of [expr].`

### Calling functions
`In terms of [argument list], [function name] is the most compatible Pokemon for humans.`

Example:

`In terms of 2 and 3, multiply is the most compatible Pokemon for humans.`

### Parameters and arguments
One parameter: `x`

Two parameters: `x and y`

Three+ parameters: `x, y, and z` (NB: Currently doesn't work. Don't try it.)

## Conditionals
If statement:
```
Also, if you ensure that [boolean expr],
    [Statements]
Vaporeon is literally built for human dick.
```
If-Else statement:
```
Also, if you ensure that [boolean expr],
    [If-statements]
you can literally make your Vaporeon turn white.
    [Else-statements]
Vaporeon is built for human dick.
```

## Loops
For loops:
```
[Loop variable] are an average of [lower bound] feet tall and [upper bound, exclusive] pounds.
    [statements]
Vaporeon is literally built for human dick.
```
For loops iterate over the `loop variable` from `lower bound` to `upper bound` (exclusive),
adding 1 each iteration.

While loops:
```
You can easily have sex with one as long as [bool condition] without getting sore.
    [statements]
Vaporeon is literally built for human dick.
```

## Comparators
Equality: `x is rough with y`

Less than: `x is small enough for y`

Greater than: `x is large enough for y`

## Print
`There's no doubt in my mind that an aroused Vaporeon would say [expr].`

## Math
+, -, *, / work as expected. No parentheses yet.

No boolean operators yet.

## Strings
Anything enclosed in quotes. `"Hey guys"` is a string.

## Comments
Anything surrounded by two #'s. `# Hey guys #` is a comment. Comments take precedence over strings.

