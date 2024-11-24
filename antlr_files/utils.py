from antlr_files.BoardGameLexer import BoardGameLexer

class utils:
    def get_literal_name(index):
        return BoardGameLexer.literalNames[index].strip("'")