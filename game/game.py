from game.models.BoardGameModel import BoardGame

def checkers():
    game = BoardGame("checkers")
    game.set_board(8, 8, "checker")
    print(f"\n{game.board.board_type} Board:")
    game.display_board()

    game.add_player("me")
    game.add_player("you")

def snakes_and_ladders():
    game2 = BoardGame("snakes_and_ladders")
    game2.set_board(10, 10, "zigzag")
    print(f"\n{game2.board.board_type} Board:")
    game2.display_board()

def go():
    game3 = BoardGame("Go")
    game3.set_board(19, 19, "intersect")
    print(f"\n{game3.board.board_type} Board:")
    game3.display_board()
    # game.run()

if __name__ == "__main__":
    checkers()
    snakes_and_ladders()
    go()