# deoplete-better-length-matcher.nvim

A replacement matcher for [Deoplete](https://github.com/Shougo/deoplete.nvim)'s `matcher_length`.

## Usage

After loading your plugins (including this one), do:

``` .vim
call deoplete#custom#set('_', 'matchers', ['matcher_better_length', 'matcher_fuzzy'])
```

## Links

* [Deoplete issue #445](https://github.com/Shougo/deoplete.nvim/pull/445)
