"""Alloy operator-to-English mappings.

The keys in STATIC_MAPPING are regular-expression replacement keys. They are
kept in descending key length so longer operators are tried before prefixes.
"""

from __future__ import annotations

import re


# Alloy 6 temporal keywords are kept for newer models, but they are outside
# older Alloy 4/5 PDF profiles that do not list temporal logic keywords.
ALLOY6_TEMPORAL_EXTENSION_KEYS = {
    r"\bafter\b",
    r"\balways\b",
    r"\bbefore\b",
    r"\beventually\b",
    r"\bhistorically\b",
    r"\bonce\b",
    r"\breleases\b",
    r"\bsince\b",
    r"\btriggered\b",
    r"\buntil\b",
    r";",
    r"'",
}


STATIC_MAPPING = {
    r"\bhistorically\b": "historically, at every previous state up to and including the current state",
    r"\beventually\b": "eventually, at some current or future state",
    r"\btriggered\b": "triggered by",
    r"\breleases\b": "releases",
    r"\bimplies\b": "implies",
    r"\balways\b": "always, at every current or future state",
    r"\bbefore\b": "before, in the immediately previous state",
    r"\bnot\s+in\b": "is not a subset of",
    r"\bnot\s+>=": "is not greater than or equal to",
    r"\bnot\s+=<": "is not less than or equal to",
    r"\bnot\s+=": "is not equal to",
    r"\bnot\s+<": "is not less than",
    r"\bnot\s+>": "is not greater than",
    r"\bexactly\b": "exactly",
    r"\bextends\b": "extends as a subtype of",
    r"\babstract\b": "abstract",
    r"\bmodule\b": "module declaration",
    r"\bafter\b": "after, in the immediately next state",
    r"\bsince\b": "since",
    r"\buntil\b": "until",
    r"\bassert\b": "assertion declaration",
    r"\bminus\b": "integer subtraction",
    r"\bplus\b": "integer addition",
    r"\bdisj\b": "pairwise disjoint",
    r"\bthis\b": "the current receiver value",
    r"\bnone\b": "the empty relation",
    r"\buniv\b": "the universal set of live atoms in the current state",
    r"\biden\b": "the identity relation over univ",
    r"\bsome\b": "one or more",
    r"\belse\b": "otherwise",
    r"\bonce\b": "once, in some previous state up to and including the current state",
    r"\bfact\b": "fact declaration",
    r"\bcheck\b": "verify the assertion",
    r"\bopen\b": "module import",
    r"\bnot\b": "not",
    r"\blone\b": "zero or one, that is, at most one",
    r"\bone\b": "exactly one",
    r"\bset\b": "any number of",
    r"\blet\b": "local binding",
    r"\bsum\b": "the arithmetic sum",
    r"\ball\b": "for all",
    r"\biff\b": "if and only if",
    r"\bInt\b": "the built-in integer type",
    r"\bmul\b": "integer multiplication",
    r"\bfun\b": "function declaration",
    r"\bdiv\b": "integer division",
    r"\bas\b": "module alias",
    r"\brem\b": "integer remainder",
    r"\band\b": "and",
    r"\bpred\b": "predicate declaration",
    r"\bno\b": "no",
    r"\bor\b": "or",
    r"\bin\b": "is a subset of",
    r"\bsig\b": "signature",
    r"\brun\b": "search for an instance",
    r"\bvar\b": "mutable",
    r"\bfor\b": "within scope",
    r"\bbut\b": "except with the following type scopes",
    r"!\s*in\b": "is not a subset of",
    r"!\s*>=": "is not greater than or equal to",
    r"!\s*=<": "is not less than or equal to",
    r"!\s*=": "is not equal to",
    r"!\s*<": "is not less than",
    r"!\s*>": "is not greater than",
    r"/\*": "start of a block comment",
    r"\*/": "end of a block comment",
    r"<=>": "if and only if",
    r"=>": "implies",
    r"\|\|": "or",
    r"\|": "such that",
    r"&&": "and",
    r"--": "start of a line comment",
    r"//": "start of a line comment",
    r"->": "the relational product arrow",
    r"<:": "domain restriction",
    r":>": "range restriction",
    r"\+\+": "relational override",
    r"\[\]": "box join brackets",
    r"\{\}": "block braces",
    r"\(\)": "precedence grouping parentheses",
    r">=": "is greater than or equal to",
    r"=<": "is less than or equal to",
    r"\#": "the cardinality of",
    r"\~": "the transpose of",
    r"\^": "the transitive closure of",
    r"\*": "the reflexive-transitive closure of",
    r"\&": "intersection",
    r"\+": "union",
    r"\-": "difference",
    r"\.": "join",
    r";": "and then, in the next state",
    r"\[": "start of box join, parameter list, or optional grammar group",
    r"\]": "end of box join, parameter list, or optional grammar group",
    r"\{": "start of a block",
    r"\}": "end of a block",
    r"\(": "start of a parenthesized expression or parameter declaration list",
    r"\)": "end of a parenthesized expression or parameter declaration list",
    r":": "of type",
    r",": "and, in a comma-separated list",
    r"/": "qualified-name or module-path separator",
    r"=": "is equal to",
    r"<": "is less than",
    r">": "is greater than",
    r"!": "not",
    r"'": "the value in the next state",
    r"@": "the non-implicitly-dereferenced name",
}

STATIC_MAPPING = dict(
    sorted(STATIC_MAPPING.items(), key=lambda item: len(item[0]), reverse=True)
)

ALLOY_4_5_PDF_STATIC_MAPPING = {
    key: value
    for key, value in STATIC_MAPPING.items()
    if key not in ALLOY6_TEMPORAL_EXTENSION_KEYS
}


PATTERN_MAPPING = [
    {
        "name": "block_comment",
        "category": "comment",
        "pattern": re.compile(r"/\*(?P<comment>.*?)\*/", re.DOTALL),
        "replacement": r"Block comment ignored by Alloy: \g<comment>.",
    },
    {
        "name": "double_slash_line_comment",
        "category": "comment",
        "pattern": re.compile(r"//(?P<comment>[^\n]*)"),
        "replacement": r"Line comment ignored by Alloy: \g<comment>.",
    },
    {
        "name": "double_dash_line_comment",
        "category": "comment",
        "pattern": re.compile(r"--(?P<comment>[^\n]*)"),
        "replacement": r"Line comment ignored by Alloy: \g<comment>.",
    },
    {
        "name": "module_declaration",
        "category": "module_declaration",
        "pattern": re.compile(r"\bmodule\s+(?P<module>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)"),
        "replacement": r"Module declaration: this Alloy model is named \g<module>.",
    },
    {
        "name": "open_module_with_alias_and_arguments",
        "category": "module_import",
        "pattern": re.compile(
            r"\bopen\s+(?P<module>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)"
            r"\s*\[\s*(?P<args>[^\]]*)\s*\]\s+as\s+(?P<alias>[A-Za-z_]\w*)"
        ),
        "replacement": r"Import module \g<module> with actual arguments \g<args> and refer to it using alias \g<alias>.",
    },
    {
        "name": "open_module_with_alias",
        "category": "module_import",
        "pattern": re.compile(
            r"\bopen\s+(?P<module>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)"
            r"\s+as\s+(?P<alias>[A-Za-z_]\w*)"
        ),
        "replacement": r"Import module \g<module> and refer to it using alias \g<alias>.",
    },
    {
        "name": "open_module_with_arguments",
        "category": "module_import",
        "pattern": re.compile(
            r"\bopen\s+(?P<module>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)"
            r"\s*\[\s*(?P<args>[^\]]*)\s*\](?!\s+as\b)"
        ),
        "replacement": r"Import module \g<module> with actual arguments \g<args>.",
    },
    {
        "name": "open_module",
        "category": "module_import",
        "pattern": re.compile(
            r"\bopen\s+(?P<module>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)"
            r"(?![\w/])(?!\s*(?:\[|as\b))"
        ),
        "replacement": r"Import module \g<module>.",
    },
    {
        "name": "qualified_this_name",
        "category": "qualified_name",
        "pattern": re.compile(r"\bthis/(?P<path>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)+)"),
        "replacement": r"The qualified name this/\g<path>, resolved from the current module namespace through slash-separated path components.",
    },
    {
        "name": "qualified_name",
        "category": "qualified_name",
        "pattern": re.compile(r"\b(?P<path>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)+)"),
        "replacement": r"The slash-qualified name \g<path>.",
    },
    {
        "name": "named_fact_declaration",
        "category": "paragraph_declaration",
        "pattern": re.compile(r"\bfact\s+(?P<name>[A-Za-z_]\w*)\s*\{\s*(?P<body>[^}]*)\s*\}"),
        "replacement": r"Fact \g<name> declares a constraint that must hold in every instance: \g<body>.",
    },
    {
        "name": "anonymous_fact_declaration",
        "category": "paragraph_declaration",
        "pattern": re.compile(r"\bfact\s*\{\s*(?P<body>[^}]*)\s*\}"),
        "replacement": r"Anonymous fact declares a constraint that must hold in every instance: \g<body>.",
    },
    {
        "name": "assertion_declaration",
        "category": "paragraph_declaration",
        "pattern": re.compile(r"\bassert\s+(?P<name>[A-Za-z_]\w*)\s*\{\s*(?P<body>[^}]*)\s*\}"),
        "replacement": r"Assertion \g<name> declares a property intended to be checked for counterexamples: \g<body>.",
    },
    {
        "name": "predicate_declaration_with_parameters",
        "category": "paragraph_declaration",
        "pattern": re.compile(
            r"\bpred\s+(?P<name>[A-Za-z_]\w*)"
            r"\s*\[\s*(?P<params>[^\]]*)\s*\]\s*\{\s*(?P<body>[^}]*)\s*\}"
        ),
        "replacement": r"Predicate \g<name> with parameters \g<params> defines a reusable Boolean constraint: \g<body>.",
    },
    {
        "name": "predicate_declaration",
        "category": "paragraph_declaration",
        "pattern": re.compile(r"\bpred\s+(?P<name>[A-Za-z_]\w*)\s*\{\s*(?P<body>[^}]*)\s*\}"),
        "replacement": r"Predicate \g<name> defines a reusable Boolean constraint: \g<body>.",
    },
    {
        "name": "function_declaration_with_parameters",
        "category": "paragraph_declaration",
        "pattern": re.compile(
            r"\bfun\s+(?P<name>[A-Za-z_]\w*)"
            r"\s*\[\s*(?P<params>[^\]]*)\s*\]\s*:\s*(?P<return>[^{}\n]+?)"
            r"\s*\{\s*(?P<body>[^}]*)\s*\}"
        ),
        "replacement": r"Function \g<name> with parameters \g<params> returns a value of type \g<return> defined by \g<body>.",
    },
    {
        "name": "function_declaration",
        "category": "paragraph_declaration",
        "pattern": re.compile(
            r"\bfun\s+(?P<name>[A-Za-z_]\w*)\s*:\s*(?P<return>[^{}\n]+?)"
            r"\s*\{\s*(?P<body>[^}]*)\s*\}"
        ),
        "replacement": r"Function \g<name> returns a value of type \g<return> defined by \g<body>.",
    },
    {
        "name": "integer_type_declaration",
        "category": "type_declaration",
        "pattern": re.compile(r"(?P<var>[A-Za-z_]\w*)\s*:\s*Int\b"),
        "replacement": r"\g<var> is constrained by default to exactly one atom drawn from the built-in integer type Int.",
    },
    {
        "name": "modified_signature_extends_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(
            r"\b(?P<modifiers>(?:(?:abstract|one|lone|some|var)\s+)+)"
            r"sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s+extends\s+(?P<parent>[A-Za-z_]\w*)"
        ),
        "replacement": r"Each signature in \g<sigs> is declared with Alloy modifiers \g<modifiers>; each is a subtype of \g<parent>.",
    },
    {
        "name": "signature_extends_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(r"\bsig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s+extends\s+(?P<parent>[A-Za-z_]\w*)"),
        "replacement": r"Each signature in \g<sigs> is a subtype of \g<parent>.",
    },
    {
        "name": "modified_signature_subset_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(
            r"\b(?P<modifiers>(?:(?:abstract|one|lone|some|var)\s+)+)"
            r"sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s+in\s+"
            r"(?P<supersets>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"Each signature in \g<sigs> is declared with Alloy modifiers \g<modifiers>; each is a subset of \g<supersets>.",
    },
    {
        "name": "signature_subset_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(
            r"\bsig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s+in\s+"
            r"(?P<supersets>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"Each signature in \g<sigs> is a subset of \g<supersets>.",
    },
    {
        "name": "abstract_modified_signature_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(
            r"\babstract\s+(?P<modifiers>(?:(?:one|lone|some|var)\s+)+)"
            r"sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"Each abstract signature in \g<sigs> has no atoms except those belonging to its extension signatures; additional modifiers: \g<modifiers>.",
    },
    {
        "name": "abstract_signature_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(r"\babstract\s+sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"),
        "replacement": r"Each abstract signature in \g<sigs> has no atoms except those belonging to its extension signatures.",
    },
    {
        "name": "one_signature_declaration",
        "category": "multiplicity_declaration",
        "pattern": re.compile(r"\bone\s+(?:var\s+)?sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"),
        "replacement": r"Each signature in \g<sigs> is constrained to contain exactly one atom in every relevant state.",
    },
    {
        "name": "lone_signature_declaration",
        "category": "multiplicity_declaration",
        "pattern": re.compile(r"\blone\s+(?:var\s+)?sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"),
        "replacement": r"Each signature in \g<sigs> is constrained to contain zero or one atom in every relevant state.",
    },
    {
        "name": "some_signature_declaration",
        "category": "multiplicity_declaration",
        "pattern": re.compile(r"\bsome\s+(?:var\s+)?sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"),
        "replacement": r"Each signature in \g<sigs> is constrained to contain at least one atom in every relevant state.",
    },
    {
        "name": "signature_declaration",
        "category": "signature_declaration",
        "pattern": re.compile(r"\b(?:var\s+)?sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s*(?=\{)"),
        "replacement": r"Each signature in \g<sigs> declares a set of atoms.",
    },
    {
        "name": "run_command_with_scope",
        "category": "command",
        "pattern": re.compile(
            r"\brun\s+(?P<target>[A-Za-z_]\w*|\{[^}]*\})(?!\w)\s+for\s+(?P<scope>[^{}\n]+)"
        ),
        "replacement": r"Run command: search for an instance of \g<target> within scope \g<scope>.",
    },
    {
        "name": "check_command_with_scope",
        "category": "command",
        "pattern": re.compile(
            r"\bcheck\s+(?P<target>[A-Za-z_]\w*|\{[^}]*\})(?!\w)\s+for\s+(?P<scope>[^{}\n]+)"
        ),
        "replacement": r"Check command: search for a counterexample to \g<target> within scope \g<scope>.",
    },
    {
        "name": "run_command",
        "category": "command",
        "pattern": re.compile(r"\brun\s+(?P<target>[A-Za-z_]\w*|\{[^}]*\})(?!\w)(?!\s+for\b)"),
        "replacement": r"Run command: search for an instance of \g<target>.",
    },
    {
        "name": "check_command",
        "category": "command",
        "pattern": re.compile(r"\bcheck\s+(?P<target>[A-Za-z_]\w*|\{[^}]*\})(?!\w)(?!\s+for\b)"),
        "replacement": r"Check command: search for a counterexample to \g<target>.",
    },
    {
        "name": "overall_scope_with_exceptions",
        "category": "command_scope",
        "pattern": re.compile(r"\bfor\s+(?P<overall>\d+)\s+but\s+(?P<type_scopes>[^{}\n]+)"),
        "replacement": r"Use an overall scope of \g<overall>, except where these type scopes override it: \g<type_scopes>.",
    },
    {
        "name": "exact_type_scope",
        "category": "command_scope",
        "pattern": re.compile(r"\bexactly\s+(?P<count>\d+)\s+(?P<sig>[A-Za-z_]\w*)"),
        "replacement": r"Constrain the command scope to exactly \g<count> atoms of \g<sig>.",
    },
    {
        "name": "overall_scope",
        "category": "command_scope",
        "pattern": re.compile(r"\bfor\s+(?P<scope>\d+)\b(?!\s+but\b)"),
        "replacement": r"Use an overall command scope of \g<scope>.",
    },
    {
        "name": "nested_conditional_implication_else",
        "category": "logical",
        "pattern": re.compile(
            r"(?P<outer_condition>[^{}\n]+?)\s*(?:(?<!<)=>|\bimplies\b)\s*"
            r"(?P<inner_condition>[^{}\n]+?)\s*(?:(?<!<)=>|\bimplies\b)\s*"
            r"(?P<then_branch>[^{}\n]+?)\s+\belse\b\s+"
            r"(?P<else_branch>[^{}\n]+)"
        ),
        "replacement": r"If \g<outer_condition>, then if \g<inner_condition>, then \g<then_branch>; otherwise, \g<else_branch>.",
    },
    {
        "name": "conditional_implication_else",
        "category": "logical",
        "pattern": re.compile(
            r"(?P<condition>[^{}\n]+?)\s*(?:(?<!<)=>|\bimplies\b)\s*"
            r"(?P<then_branch>[^{}\n]+?)\s+\belse\b\s+"
            r"(?P<else_branch>[^{}\n]+)"
        ),
        "replacement": r"If \g<condition>, then \g<then_branch>; otherwise, \g<else_branch>.",
    },
    {
        "name": "braced_conditional_implication_else",
        "category": "logical_expression_block",
        "pattern": re.compile(
            r"(?P<condition>[^{}\n]+?)\s*(?:(?<!<)=>|\bimplies\b)\s*"
            r"\{\s*(?P<then_body>[^{}]*)\s*\}\s+\belse\b\s+"
            r"\{\s*(?P<else_body>[^{}]*)\s*\}"
        ),
        "replacement": r"If \g<condition>, then the following block must hold: \g<then_body>; otherwise, the following block must hold: \g<else_body>.",
    },
    {
        "name": "braced_conditional_implication",
        "category": "logical_expression_block",
        "pattern": re.compile(
            r"(?P<condition>[^{}\n]+?)\s*(?:(?<!<)=>|\bimplies\b)\s*"
            r"\{\s*(?P<then_body>[^{}]*)\s*\}"
        ),
        "replacement": r"If \g<condition>, then the following block must hold: \g<then_body>.",
    },
    {
        "name": "compound_universal_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\ball\s+(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\}?"
        ),
        "replacement": r"For every binding satisfying the declarations \g<decls>, the formula after the separator must hold: \g<body>.",
    },
    {
        "name": "compound_no_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bno\s+(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There is no binding satisfying the declarations \g<decls> such that the following formula holds: \g<body>.",
    },
    {
        "name": "compound_existential_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bsome\s+(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists at least one binding satisfying the declarations \g<decls> such that the following formula holds: \g<body>.",
    },
    {
        "name": "compound_lone_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\blone\s+(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists zero or one binding satisfying the declarations \g<decls> such that the following formula holds: \g<body>.",
    },
    {
        "name": "compound_one_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bone\s+(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists exactly one binding satisfying the declarations \g<decls> such that the following formula holds: \g<body>.",
    },
    {
        "name": "compound_sum_quantifier",
        "category": "quantifier_arithmetic",
        "pattern": re.compile(
            r"\bsum\s+(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*\|\s*(?P<body>[^}\n]+)"
        ),
        "replacement": r"The integer sum over all bindings satisfying the declarations \g<decls>, evaluating the expression after the separator: \g<body>.",
    },
    {
        "name": "disjoint_universal_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\ball\s+disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"For every choice of distinct elements \g<var> drawn from \g<type>, the formula after the vertical bar must hold: \g<body>.",
    },
    {
        "name": "universal_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\ball\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"For every binding of \g<var> drawn from \g<type>, the formula after the vertical bar must hold: \g<body>.",
    },
    {
        "name": "disjoint_no_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bno\s+disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There is no choice of distinct elements \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "no_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bno\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There is no binding of \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "disjoint_existential_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bsome\s+disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists at least one choice of distinct elements \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "existential_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bsome\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists at least one binding of \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "disjoint_lone_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\blone\s+disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists zero or one choice of distinct elements \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "lone_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\blone\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists zero or one binding of \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "disjoint_one_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bone\s+disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists exactly one choice of distinct elements \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "one_quantifier",
        "category": "quantifier",
        "pattern": re.compile(
            r"\bone\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"There exists exactly one binding of \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "disjoint_sum_quantifier",
        "category": "quantifier_arithmetic",
        "pattern": re.compile(
            r"\bsum\s+disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*\|\s*"
            r"(?P<body>[^}\n]+)"
        ),
        "replacement": r"The integer sum over all choices of distinct elements \g<var> drawn from \g<type>, evaluating the expression after the separator: \g<body>.",
    },
    {
        "name": "sum_quantifier",
        "category": "quantifier_arithmetic",
        "pattern": re.compile(
            r"\bsum\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*\|\s*"
            r"(?P<body>[^}\n]+)"
        ),
        "replacement": r"The integer sum, over all bindings of \g<var> drawn from \g<type>, evaluating the expression after the separator: \g<body>.",
    },
    {
        "name": "quantifier_bar_separator",
        "category": "syntax_separator",
        "pattern": re.compile(
            r"\b(?P<quantifier>all|some|no|one|lone)\s+"
            r"(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?))\s*\|\s*(?P<body>[^}\n]+)"
        ),
        "replacement": r"The quantifier \g<quantifier> binds \g<var> over \g<type>; the vertical bar means such that and introduces this formula: \g<body>.",
    },
    {
        "name": "sum_bar_separator",
        "category": "syntax_separator",
        "pattern": re.compile(
            r"\bsum\s+(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?))\s*\|\s*(?P<body>[^}\n]+)"
        ),
        "replacement": r"The sum quantifier binds \g<var> over \g<type>; the vertical bar introduces the integer expression to sum: \g<body>.",
    },
    {
        "name": "multiple_let_bindings",
        "category": "binding",
        "pattern": re.compile(
            r"\blet\s+(?P<bindings>[A-Za-z_]\w*\s*=\s*[^,|{\n]+"
            r"(?:\s*,\s*[A-Za-z_]\w*\s*=\s*[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\}?"
        ),
        "replacement": r"Let the local bindings \g<bindings> hold; after the separator, evaluate \g<body>.",
    },
    {
        "name": "let_binding",
        "category": "binding",
        "pattern": re.compile(
            r"\blet\s+(?P<var>[A-Za-z_]\w*)\s*=\s*(?P<value>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\}?"
        ),
        "replacement": r"Let \g<var> denote \g<value>; after the separator, evaluate \g<body>.",
    },
    {
        "name": "compound_comprehension",
        "category": "relational",
        "pattern": re.compile(
            r"\{\s*(?P<decls>(?:disj\s+)?[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*"
            r"\s*:\s*(?:disj\s+)?[^,|{\n]+(?:\s*,\s*(?:disj\s+)?[A-Za-z_]\w*"
            r"(?:\s*,\s*[A-Za-z_]\w*)*\s*:\s*(?:disj\s+)?[^,|{\n]+)+)"
            r"\s*(?:\|\s*|\{\s*)(?P<body>[^}]+)\s*\}"
        ),
        "replacement": r"The comprehension relation over declarations \g<decls>, containing exactly the tuples for which the following formula holds: \g<body>.",
    },
    {
        "name": "disjoint_comprehension",
        "category": "relational",
        "pattern": re.compile(
            r"\{\s*disj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^|{\n]+?)\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\s*\}"
        ),
        "replacement": r"The relation containing pairwise-distinct tuples of \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "comprehension",
        "category": "relational",
        "pattern": re.compile(
            r"\{\s*(?P<decls>(?:disj\s+)?(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?:disj\s+)?(?P<type>[^|{\n]+?))\s*(?:\|\s*|\{\s*)"
            r"(?P<body>[^}]+)\s*\}"
        ),
        "replacement": r"The relation containing tuples of \g<var> drawn from \g<type> such that the following formula holds: \g<body>.",
    },
    {
        "name": "disjoint_predicate",
        "category": "logical",
        "pattern": re.compile(r"\bdisj\s*\[\s*(?P<args>[^\]]+?)\s*\]"),
        "replacement": r"The expressions \g<args> are pairwise disjoint.",
    },
    {
        "name": "distinct_elements_declaration",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"\bdisj\s+(?P<vars>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)+)"
            r"\s*:\s*(?P<type>[^,|{}\n]+)"
        ),
        "replacement": r"The variables \g<vars> denote distinct elements drawn from \g<type>.",
    },
    {
        "name": "declaration_over_disjoint_type",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"(?P<vars>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*disj\s+(?P<type>[^,|{}\n]+)"
        ),
        "replacement": r"The variables \g<vars> are declared over \g<type>, with the declared values required to be disjoint.",
    },
    {
        "name": "disjoint_variable_declaration",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"\bdisj\s+(?P<var>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"
            r"\s*:\s*(?P<type>[^,|{}\n]+)"
        ),
        "replacement": r"The declared variables \g<var> range over \g<type> and are required to be pairwise distinct or pairwise disjoint.",
    },
    {
        "name": "empty_box_join_brackets",
        "category": "box_join",
        "pattern": re.compile(r"(?P<relation>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)\s*\[\s*\]"),
        "replacement": r"Empty square brackets attached to \g<relation>, used as an empty argument list rather than a relational box join argument.",
    },
    {
        "name": "dotted_box_join",
        "category": "relational_invocation",
        "pattern": re.compile(
            r"(?P<relation>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)?(?:\.[A-Za-z_]\w*(?:/[A-Za-z_]\w*)?)+)"
            r"\s*\[\s*(?P<args>[^\]]+?)\s*\]"
        ),
        "replacement": r"The box join of \g<relation> with arguments \g<args>, parsed after dot joins and then left-associatively; each relational step e2[e1] is equivalent to e1.e2.",
    },
    {
        "name": "multi_argument_box_join_or_invocation",
        "category": "relational_invocation",
        "pattern": re.compile(
            r"(?P<relation>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)"
            r"\s*\[\s*(?P<args>[^,\]]+?(?:\s*,\s*[^,\]]+?)+)\s*\]"
        ),
        "replacement": r"The box join or invocation of \g<relation> with arguments \g<args>, parsed left-associatively as repeated bracket applications.",
    },
    {
        "name": "receiver_invocation",
        "category": "invocation",
        "pattern": re.compile(
            r"(?P<receiver>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)\s*\.\s*"
            r"(?P<call>[A-Za-z_]\w*)\s*\[\s*(?P<args>[^\]]*?)\s*\]"
        ),
        "replacement": r"The invocation of \g<call> with receiver \g<receiver> and arguments \g<args>.",
    },
    {
        "name": "box_join_or_invocation",
        "category": "relational_invocation",
        "pattern": re.compile(
            r"(?<!\.)\b(?P<relation>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)*)\s*\[\s*(?P<arg>[^,\]]+?)\s*\]"
        ),
        "replacement": r"The box join or invocation of \g<relation> with \g<arg>; for relational join, e2[e1] is equivalent to e1.e2.",
    },
    {
        "name": "arithmetic_plus",
        "category": "arithmetic",
        "pattern": re.compile(r"\bplus\s*\[\s*(?P<left>[^,\]]+?)\s*,\s*(?P<right>[^\]]+?)\s*\]"),
        "replacement": r"The integer sum of \g<left> and \g<right>.",
    },
    {
        "name": "arithmetic_minus",
        "category": "arithmetic",
        "pattern": re.compile(r"\bminus\s*\[\s*(?P<left>[^,\]]+?)\s*,\s*(?P<right>[^\]]+?)\s*\]"),
        "replacement": r"The integer difference obtained by subtracting \g<right> from \g<left>.",
    },
    {
        "name": "arithmetic_multiply",
        "category": "arithmetic",
        "pattern": re.compile(r"\bmul\s*\[\s*(?P<left>[^,\]]+?)\s*,\s*(?P<right>[^\]]+?)\s*\]"),
        "replacement": r"The integer product of \g<left> and \g<right>.",
    },
    {
        "name": "arithmetic_divide",
        "category": "arithmetic",
        "pattern": re.compile(r"\bdiv\s*\[\s*(?P<dividend>[^,\]]+?)\s*,\s*(?P<divisor>[^\]]+?)\s*\]"),
        "replacement": r"The integer quotient when \g<dividend> is divided by \g<divisor>.",
    },
    {
        "name": "arithmetic_remainder",
        "category": "arithmetic",
        "pattern": re.compile(r"\brem\s*\[\s*(?P<dividend>[^,\]]+?)\s*,\s*(?P<divisor>[^\]]+?)\s*\]"),
        "replacement": r"The integer remainder when \g<dividend> is divided by \g<divisor>.",
    },
    {
        "name": "sum_function",
        "category": "arithmetic",
        "pattern": re.compile(r"\bsum\s*\[\s*(?P<expr>[^\]]+?)\s*\]"),
        "replacement": r"The integer sum of the integer atoms in \g<expr>.",
    },
    {
        "name": "negative_integer",
        "category": "arithmetic",
        "pattern": re.compile(r"(?<![\w])-(?P<number>\d+)\b"),
        "replacement": r"The negative integer \g<number>.",
    },
    {
        "name": "cardinality",
        "category": "arithmetic",
        "pattern": re.compile(r"\#\s*(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The number of tuples in \g<expr>.",
    },
    {
        "name": "transpose",
        "category": "relational_unary",
        "pattern": re.compile(r"\~\s*(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The transpose of \g<expr>.",
    },
    {
        "name": "transitive_closure",
        "category": "relational_unary",
        "pattern": re.compile(r"\^\s*(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The transitive closure of \g<expr>.",
    },
    {
        "name": "reflexive_transitive_closure",
        "category": "relational_unary",
        "pattern": re.compile(r"\*\s*(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The reflexive-transitive closure of \g<expr>.",
    },
    {
        "name": "prime_next_state",
        "category": "temporal_relational",
        "pattern": re.compile(r"(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)\s*'"),
        "replacement": r"The value of \g<expr> in the next state.",
    },
    {
        "name": "domain_restriction",
        "category": "relational_binary",
        "pattern": re.compile(r"(?P<domain>[^{}\[\]\n|]+?)\s*<:\s*(?P<relation>[^{}\[\]\n|]+)"),
        "replacement": r"The domain restriction of \g<relation> to \g<domain>.",
    },
    {
        "name": "range_restriction",
        "category": "relational_binary",
        "pattern": re.compile(r"(?P<relation>[^{}\[\]\n|]+?)\s*:>\s*(?P<range>[^{}\[\]\n|]+)"),
        "replacement": r"The range restriction of \g<relation> to \g<range>.",
    },
    {
        "name": "relational_override",
        "category": "relational_binary",
        "pattern": re.compile(r"(?P<base>[^{}\[\]\n|]+?)\s*\+\+\s*(?P<override>[^{}\[\]\n|]+)"),
        "replacement": r"The relational override of \g<base> by \g<override>.",
    },
    {
        "name": "one_to_one_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"one\s*->\s*one\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A one-to-one relation from \g<domain> to \g<range>: each domain tuple maps to exactly one range tuple, and each range tuple is mapped from exactly one domain tuple.",
    },
    {
        "name": "one_to_many_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"one\s*->\s*some\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A one-to-many relation from \g<domain> to \g<range>: each domain tuple maps to one or more range tuples, and each range tuple is mapped from exactly one domain tuple.",
    },
    {
        "name": "one_to_partial_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"one\s*->\s*lone\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A one-to-partial relation from \g<domain> to \g<range>: each domain tuple maps to zero or one range tuple, and each range tuple is mapped from exactly one domain tuple.",
    },
    {
        "name": "partial_to_one_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"lone\s*->\s*one\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A partial-to-one relation from \g<domain> to \g<range>: each domain tuple maps to exactly one range tuple, and each range tuple is mapped from zero or one domain tuple.",
    },
    {
        "name": "partial_to_partial_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"lone\s*->\s*lone\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A partial-to-partial relation from \g<domain> to \g<range>: each side is associated with zero or one tuple on the other side.",
    },
    {
        "name": "many_to_one_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"set\s*->\s*one\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A many-to-one total function-like relation from \g<domain> to \g<range>: each domain tuple maps to exactly one range tuple, and each range tuple may be mapped from any number of domain tuples.",
    },
    {
        "name": "partial_function_arrow_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"set\s*->\s*lone\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"A many-to-at-most-one partial function-like relation from \g<domain> to \g<range>: each domain tuple maps to zero or one range tuple.",
    },
    {
        "name": "set_to_set_arrow_multiplicity_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"set\s*->\s*set\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"The product from \g<domain> to \g<range> with set-to-set arrow multiplicity, imposing no default one constraint on either side.",
    },
    {
        "name": "arrow_multiplicity_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"(?P<left_mult>lone|one|some|set)\s*->\s*"
            r"(?P<right_mult>lone|one|some|set)\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"The product from \g<domain> to \g<range>, constraining each range tuple to have \g<left_mult> ending tuples and each domain tuple to have \g<right_mult> beginning tuples.",
    },
    {
        "name": "right_arrow_multiplicity_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s*->\s*"
            r"(?P<right_mult>lone|one|some|set)\s+"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"The product from \g<domain> to \g<range>, constraining each domain tuple to have \g<right_mult> beginning tuples.",
    },
    {
        "name": "left_arrow_multiplicity_product",
        "category": "multiplicity_relational",
        "pattern": re.compile(
            r"\b(?P<domain>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)\s+"
            r"(?P<left_mult>lone|one|some|set)\s*->\s*"
            r"(?P<range>(?!set\b|one\b|lone\b|some\b)[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"The product from \g<domain> to \g<range>, constraining each range tuple to have \g<left_mult> ending tuples.",
    },
    {
        "name": "relational_product",
        "category": "relational_binary",
        "pattern": re.compile(
            r"(?P<left>[^{}\[\]\n|]+?)\s*"
            r"(?<!set\s)(?<!one\s)(?<!lone\s)(?<!some\s)->(?!\s*(?:set|one|lone|some)\b)"
            r"\s*(?P<right>[^{}\[\]\n|]+)"
        ),
        "replacement": r"The relational product of \g<left> and \g<right>.",
    },
    {
        "name": "relational_join",
        "category": "relational_binary",
        "pattern": re.compile(
            r"(?P<left>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)?(?:\.[A-Za-z_]\w*)*)"
            r"\s*\.\s*"
            r"(?P<right>[A-Za-z_]\w*(?:/[A-Za-z_]\w*)?)"
        ),
        "replacement": r"The relational join of \g<left> and \g<right>.",
    },
    {
        "name": "relational_intersection",
        "category": "relational_binary",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*&\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"The intersection of \g<left> and \g<right>.",
    },
    {
        "name": "relational_union",
        "category": "relational_binary",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*\+\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"The union of \g<left> and \g<right>.",
    },
    {
        "name": "relational_difference",
        "category": "relational_binary",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*-(?!>)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"The tuples in \g<left> that are not in \g<right>.",
    },
    {
        "name": "not_subset",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:!\s*in|\bnot\s+in\b)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"It is not the case that \g<left> is a subset of \g<right>.",
    },
    {
        "name": "not_equal",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:!\s*=(?![<>])|\bnot\s+=(?![<>]))\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is not equal to \g<right>.",
    },
    {
        "name": "not_less_than_or_equal",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:!\s*=<|\bnot\s+=<)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is not less than or equal to \g<right>.",
    },
    {
        "name": "not_greater_than_or_equal",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:!\s*>=|\bnot\s+>=)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is not greater than or equal to \g<right>.",
    },
    {
        "name": "not_less_than",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:!\s*<|\bnot\s+<)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is not less than \g<right>.",
    },
    {
        "name": "not_greater_than",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:!\s*>(?!=)|\bnot\s+>(?!=))\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is not greater than \g<right>.",
    },
    {
        "name": "subset",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s+\bin\b\s+(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is a subset of \g<right>.",
    },
    {
        "name": "equality",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|=!<>]+?)\s*=(?![<>])\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is equal to \g<right>.",
    },
    {
        "name": "less_than_or_equal",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?<!!)=<\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is less than or equal to \g<right>.",
    },
    {
        "name": "greater_than_or_equal",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?<!!)>=\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is greater than or equal to \g<right>.",
    },
    {
        "name": "less_than",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|=<]+?)\s*(?<!!)<(?![:=>])\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is less than \g<right>.",
    },
    {
        "name": "greater_than",
        "category": "comparison",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|=>]+?)\s*(?<![-=!])>(?!=)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> is greater than \g<right>.",
    },
    {
        "name": "boolean_negation",
        "category": "logical",
        "pattern": re.compile(r"(?:!|\bnot\b)\s*(?P<formula>[A-Za-z_]\w*(?:\[[^\]]*\])?)"),
        "replacement": r"It is not the case that \g<formula>.",
    },
    {
        "name": "logical_equivalence",
        "category": "logical",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:<=>|\biff\b)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"\g<left> holds if and only if \g<right> holds.",
    },
    {
        "name": "logical_implication",
        "category": "logical",
        "pattern": re.compile(r"(?P<antecedent>[^{}\[\]\n|]+?)\s*(?:(?<!<)=>|\bimplies\b)\s*(?P<consequent>[^{}\[\]\n|]+)"),
        "replacement": r"If \g<antecedent>, then \g<consequent>.",
    },
    {
        "name": "logical_conjunction",
        "category": "logical",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:&&|\band\b)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"Both \g<left> and \g<right> hold.",
    },
    {
        "name": "logical_disjunction",
        "category": "logical",
        "pattern": re.compile(r"(?P<left>[^{}\[\]\n|]+?)\s*(?:\|\||\bor\b)\s*(?P<right>[^{}\[\]\n|]+)"),
        "replacement": r"At least one of \g<left> or \g<right> holds.",
    },
    {
        "name": "no_expression",
        "category": "multiplicity_expression",
        "pattern": re.compile(r"\bno\s+(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The relation \g<expr> contains no tuples.",
    },
    {
        "name": "some_expression",
        "category": "multiplicity_expression",
        "pattern": re.compile(r"\bsome\s+(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The relation \g<expr> contains at least one tuple.",
    },
    {
        "name": "lone_expression",
        "category": "multiplicity_expression",
        "pattern": re.compile(r"\blone\s+(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The relation \g<expr> contains zero or one tuple.",
    },
    {
        "name": "one_expression",
        "category": "multiplicity_expression",
        "pattern": re.compile(r"\bone\s+(?P<expr>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)"),
        "replacement": r"The relation \g<expr> contains exactly one tuple.",
    },
    {
        "name": "set_declaration_multiplicity",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"(?P<var>[A-Za-z_]\w*)\s*:\s*set\s+(?P<type>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"\g<var> may contain any number of elements drawn from \g<type>.",
    },
    {
        "name": "lone_declaration_multiplicity",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"(?P<var>[A-Za-z_]\w*)\s*:\s*lone\s+(?P<type>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"\g<var> is constrained to contain zero or one element drawn from \g<type>.",
    },
    {
        "name": "some_declaration_multiplicity",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"(?P<var>[A-Za-z_]\w*)\s*:\s*some\s+(?P<type>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"\g<var> is constrained to contain at least one element drawn from \g<type>.",
    },
    {
        "name": "one_declaration_multiplicity",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"(?P<var>[A-Za-z_]\w*)\s*:\s*one\s+(?P<type>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"\g<var> is constrained to contain exactly one element drawn from \g<type>.",
    },
    {
        "name": "multi_variable_type_declaration",
        "category": "type_declaration",
        "pattern": re.compile(
            r"(?P<vars>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)+)\s*:\s*(?P<type>[^,|{}\n]+)"
        ),
        "replacement": r"The comma-separated variables \g<vars> are declared to be of type \g<type>.",
    },
    {
        "name": "type_declaration_separator",
        "category": "type_declaration",
        "pattern": re.compile(r"(?P<var>[A-Za-z_]\w*)\s*:\s*(?P<type>[^,|{}\n]+)"),
        "replacement": r"\g<var> is declared to be of type \g<type>.",
    },
    {
        "name": "default_unary_declaration_multiplicity",
        "category": "multiplicity_declaration",
        "pattern": re.compile(
            r"(?P<var>[A-Za-z_]\w*)\s*:\s*(?P<type>[A-Za-z_]\w*(?:\s*\+\s*[A-Za-z_]\w*)*)"
        ),
        "replacement": r"\g<var> is constrained by default to exactly one element drawn from \g<type>.",
    },
    {
        "name": "signature_multiplicity",
        "category": "multiplicity_declaration",
        "pattern": re.compile(r"\b(?P<mult>lone|some|one)\s+(?:var\s+)?sig\s+(?P<sigs>[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)"),
        "replacement": r"Each signature in \g<sigs> is constrained to have \g<mult> elements in every state.",
    },
    {
        "name": "braced_block",
        "category": "scope_boundary",
        "pattern": re.compile(r"\{\s*(?P<body>[^{}]*)\s*\}"),
        "replacement": r"A block delimited by braces containing: \g<body>.",
    },
    {
        "name": "parenthesized_expression",
        "category": "scope_boundary",
        "pattern": re.compile(r"\(\s*(?P<expr>[^()]*)\s*\)"),
        "replacement": r"A parenthesized expression that groups and prioritizes: \g<expr>.",
    },
    {
        "name": "future_after",
        "category": "temporal_logical",
        "pattern": re.compile(r"\bafter\s+(?P<formula>[^{}\n;]+)"),
        "replacement": r"\g<formula> holds in the immediately next state.",
    },
    {
        "name": "future_always",
        "category": "temporal_logical",
        "pattern": re.compile(r"\balways\s+(?P<formula>[^{}\n;]+)"),
        "replacement": r"\g<formula> holds in every current and future state.",
    },
    {
        "name": "future_eventually",
        "category": "temporal_logical",
        "pattern": re.compile(r"\beventually\s+(?P<formula>[^{}\n;]+)"),
        "replacement": r"\g<formula> holds in some current or future state.",
    },
    {
        "name": "future_until",
        "category": "temporal_logical",
        "pattern": re.compile(r"(?P<left>[^{}\n;]+?)\s+\buntil\b\s+(?P<right>[^{}\n;]+)"),
        "replacement": r"\g<right> eventually holds, and \g<left> holds until before that state.",
    },
    {
        "name": "future_releases",
        "category": "temporal_logical",
        "pattern": re.compile(r"(?P<left>[^{}\n;]+?)\s+\breleases\b\s+(?P<right>[^{}\n;]+)"),
        "replacement": r"\g<right> holds until and including a state where \g<left> holds, or \g<right> holds forever if no such state occurs.",
    },
    {
        "name": "temporal_sequence",
        "category": "temporal_logical",
        "pattern": re.compile(r"(?P<current>[^{}\n;]+?)\s*;\s*(?P<next>[^{}\n;]+)"),
        "replacement": r"\g<current> holds now, and \g<next> holds in the immediately next state.",
    },
    {
        "name": "past_before",
        "category": "temporal_logical",
        "pattern": re.compile(r"\bbefore\s+(?P<formula>[^{}\n;]+)"),
        "replacement": r"\g<formula> holds in the immediately previous state; this is false in the initial state.",
    },
    {
        "name": "past_historically",
        "category": "temporal_logical",
        "pattern": re.compile(r"\bhistorically\s+(?P<formula>[^{}\n;]+)"),
        "replacement": r"\g<formula> holds in every previous state up to and including the current state.",
    },
    {
        "name": "past_once",
        "category": "temporal_logical",
        "pattern": re.compile(r"\bonce\s+(?P<formula>[^{}\n;]+)"),
        "replacement": r"\g<formula> holds in some previous state up to and including the current state.",
    },
    {
        "name": "past_since",
        "category": "temporal_logical",
        "pattern": re.compile(r"(?P<left>[^{}\n;]+?)\s+\bsince\b\s+(?P<right>[^{}\n;]+)"),
        "replacement": r"\g<right> held at some previous state, and \g<left> has held continuously since after that state through now.",
    },
    {
        "name": "past_triggered",
        "category": "temporal_logical",
        "pattern": re.compile(r"(?P<left>[^{}\n;]+?)\s+\btriggered\b\s+(?P<right>[^{}\n;]+)"),
        "replacement": r"\g<right> has held continuously since after a previous state where \g<left> held, or \g<right> has always held if no such previous state exists.",
    },
]

ALLOY6_TEMPORAL_EXTENSION_PATTERN_NAMES = {
    "future_after",
    "future_always",
    "future_eventually",
    "future_releases",
    "future_until",
    "past_before",
    "past_historically",
    "past_once",
    "past_since",
    "past_triggered",
    "prime_next_state",
    "temporal_sequence",
}

ALLOY_4_5_PDF_PATTERN_MAPPING = [
    item
    for item in PATTERN_MAPPING
    if item["name"] not in ALLOY6_TEMPORAL_EXTENSION_PATTERN_NAMES
    and not item["category"].startswith("temporal_")
]

# ---------------------------------------------------------------------
# Controlled English fallback helpers
# ---------------------------------------------------------------------


CONTROLLED_ENGLISH_STATIC_MAPPING = {
    r"\bimplies\b": "implies",
    r"=>": "implies",
    r"\biff\b": "if and only if",
    r"<=>": "if and only if",
    r"\band\b": "and",
    r"&&": "and",
    r"\bor\b": "or",
    r"\|\|": "or",
    r"\bnot\b": "not",
    r"\bin\b": "is in",
    r"!\s*in\b": "is not in",
    r"\bnot\s+in\b": "is not in",
    r"!=": "does not equal",
    r"!\s*=": "does not equal",
    r">=": "is greater than or equal to",
    r"=<": "is less than or equal to",
    r"<=": "is less than or equal to",
    r">": "is greater than",
    r"<": "is less than",
    r"=": "equals",
    r"\#": "the cardinality of",
    r"->": "arrow",
    r"\+": "plus",
    r"\-": "minus",
    r"\&": "intersect",
    r"\+\+": "override",
    r"<:": "domain restriction",
    r":>": "range restriction",
    r"\~": "transpose",
    r"\^": "transitive closure",
    r"\*": "reflexive transitive closure",
}


CONTROLLED_ENGLISH_STATIC_MAPPING = dict(
    sorted(CONTROLLED_ENGLISH_STATIC_MAPPING.items(), key=lambda item: len(item[0]), reverse=True)
)


def explain_with_patterns(text: str, alloy_version: str = "4_5") -> str:
    """
    Fallback explanation for syntax not handled by controlled_english_translator.py.

    Important:
    - This function should be used only as fallback.
    - Do not use it as the main translator.
    - It intentionally avoids global replacement of '.' because the controlled
      English pipeline preserves names such as p.steps.
    """
    stripped = text.strip()

    pattern_mapping = (
        ALLOY_4_5_PDF_PATTERN_MAPPING
        if alloy_version == "4_5" and "ALLOY_4_5_PDF_PATTERN_MAPPING" in globals()
        else PATTERN_MAPPING
    )

    for item in pattern_mapping:
        pattern = item.get("pattern")
        replacement = item.get("replacement")
        if pattern is None or replacement is None:
            continue

        match = pattern.fullmatch(stripped)
        if match:
            return match.expand(replacement)

    return explain_with_static_mapping(stripped)


def explain_with_static_mapping(text: str) -> str:
    """
    Controlled fallback static explanation.

    This is conservative:
    - It does not replace '.'.
    - It does not try to interpret p.steps = A -> B as a sequence.
      That is handled in controlled_english_translator.py.
    """
    result = text

    for pattern, replacement in CONTROLLED_ENGLISH_STATIC_MAPPING.items():
        if pattern == r"\.":
            continue
        result = re.sub(pattern, replacement, result)

    if result != text:
        return result

    return text