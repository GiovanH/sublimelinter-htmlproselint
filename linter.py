from SublimeLinter.lint import Linter  # type: ignore[import]  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

class MdProseLint(Linter):
    cmd = ('mdproselint', '${args}')
    linefmt = r'{line}:\({col}, {end_col}\) {error_type} {code} "{message}"'
    regex = linefmt.format(
        line=r"(?P<line>.+?)",
        code=r"(?P<code>.+?)",
        col=r"(?P<col>.+?)",
        end_col=r"(?P<end_col>.+?)",
        message=r"(?P<message>.+?)",
        error_type=r"(?P<error_type>.+?)"
    ) + r"$"

    multiline = False
    defaults = {
        'selector': 'text.html.markdown'
    }

    line_col_base = (0, 0)