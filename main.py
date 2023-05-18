import tests.test_tic_tac_toe
import src.algorithms.minmax
from src.games.tic_tac_toe import TicTacToe
import numpy as np

def get_better_move(game):
    posible_moves = game.all_posibles_moves()
    actual_status = game.board

    best_move = np.argmax([minmax(move) for move in game.all_posibles_moves()])
    return best_move


def get_score(game):
    if game.winner is None or 'Draw':
        return 0
    elif game.winner == 'X':
        return -1
    elif game.winner == 'O':
        return 1



def minmax(game, move, maximazing, depth):
    game.make_move(move)
    if game.is_finish is True:
        return get_score(game)


    if maximazing is True:
        ### Complete
        return True
    else:
        ### Complete
        return False


if __name__ == '__main__':
    ttt = TicTacToe()


# Daniel code
'''




int minimax(char[][] board, int depth, boolean isMaximizing) {
  char result = checkWinner();
  if (result != 'n') {
    return scores.get(result);
  }

  if (isMaximizing) {
    int bestScore = Integer.MIN_VALUE;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        // Is the spot available?
        if (board[i][j] == (char)0) {
          board[i][j] = ai;
          int score = minimax(board, depth + 1, false);
          board[i][j] = (char)0;
          bestScore = max(score, bestScore);
        }
      }
    }
    return bestScore;
  } else {
    int bestScore = Integer.MAX_VALUE;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        // Is the spot available?
        if (board[i][j] == (char)0) {
          board[i][j] = human;
          int score = minimax(board, depth + 1, true);
          board[i][j] = (char)0;
          bestScore = min(score, bestScore);
        }
      }
    }
    return bestScore;
  }
}
















// Tic Tac Toe AI with Minimax Algorithm
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/challenges/154-tic-tac-toe-minmax
// https://youtu.be/I64-UTORVfU
// https://editor.p5js.org/codingtrain/sketches/0zyUhZdJD

let board = [
  ['', '', ''],
  ['', '', ''],
  ['', '', '']
];

let w; // = width / 3;
let h; // = height / 3;

let ai = 'X';
let human = 'O';
let currentPlayer = human;

function setup() {
  createCanvas(400, 400);
  w = width / 3;
  h = height / 3;
  bestMove();
}

function equals3(a, b, c) {
  return a == b && b == c && a != '';
}

function checkWinner() {
  let winner = null;

  // horizontal
  for (let i = 0; i < 3; i++) {
    if (equals3(board[i][0], board[i][1], board[i][2])) {
      winner = board[i][0];
    }
  }

  // Vertical
  for (let i = 0; i < 3; i++) {
    if (equals3(board[0][i], board[1][i], board[2][i])) {
      winner = board[0][i];
    }
  }

  // Diagonal
  if (equals3(board[0][0], board[1][1], board[2][2])) {
    winner = board[0][0];
  }
  if (equals3(board[2][0], board[1][1], board[0][2])) {
    winner = board[2][0];
  }

  let openSpots = 0;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (board[i][j] == '') {
        openSpots++;
      }
    }
  }

  if (winner == null && openSpots == 0) {
    return 'tie';
  } else {
    return winner;
  }
}

function mousePressed() {
  if (currentPlayer == human) {
    // Human make turn
    let i = floor(mouseX / w);
    let j = floor(mouseY / h);
    // If valid turn
    if (board[i][j] == '') {
      board[i][j] = human;
      currentPlayer = ai;
      bestMove();
    }
  }
}

function draw() {
  background(255);
  strokeWeight(4);

  line(w, 0, w, height);
  line(w * 2, 0, w * 2, height);
  line(0, h, width, h);
  line(0, h * 2, width, h * 2);

  for (let j = 0; j < 3; j++) {
    for (let i = 0; i < 3; i++) {
      let x = w * i + w / 2;
      let y = h * j + h / 2;
      let spot = board[i][j];
      textSize(32);
      let r = w / 4;
      if (spot == human) {
        noFill();
        ellipse(x, y, r * 2);
      } else if (spot == ai) {
        line(x - r, y - r, x + r, y + r);
        line(x + r, y - r, x - r, y + r);
      }
    }
  }

  let result = checkWinner();
  if (result != null) {
    noLoop();
    let resultP = createP('');
    resultP.style('font-size', '32pt');
    if (result == 'tie') {
      resultP.html('Tie!');
    } else {
      resultP.html(`${result} wins!`);
    }
  }
}

-------------- Java ---------------------
void bestMove() {
  // AI to make its turn
  int bestScore = Integer.MIN_VALUE;
  int[] move = {0, 0};
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      // Is the spot available?
      if (board[i][j] == (char)0) {
        board[i][j] = ai;
        int score = minimax(board, 0, false);
        board[i][j] = (char)0;
        if (score > bestScore) {
          bestScore = score;
          move[0] = i;
          move[1] = j;
        }
      }
    }
  }
  board[move[0]][move[1]] = ai;
  currentPlayerIsHuman = true;
}




'''
