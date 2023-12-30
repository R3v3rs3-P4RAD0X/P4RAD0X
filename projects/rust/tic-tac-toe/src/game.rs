pub mod game {
    pub struct Game {
        pub board: Board,
        players: [Player; 2],
        turn: u8,
    }

    pub struct Player {
        symbol: char,
        score: u8,
    }

    pub struct Board {
        cells: [[char; 3]; 3],
    }

    // Implementation of Game, Player, and Board structs
    impl Game {
        pub fn new() -> Game {
            Game {
                board: Board::new(),
                players: [Player::new('X'), Player::new('O')],
                turn: 0,
            }
        }

        fn clear_screen(&self) {
            let _ = if cfg!(target_os = "windows") {
                std::process::Command::new("cmd")
                    .args(&["/C", "cls"])
                    .status()
            } else {
                std::process::Command::new("sh")
                    .args(&["-c", "clear"])
                    .status()
            };
        }

        pub fn play(&mut self) {
            loop {
                self.clear_screen();
                self.board.display();
                self.take_turn();
                if self.check_board() {
                    self.clear_screen();

                    // Display the final board
                    self.board.display();

                    // Print the winner
                    println!("Player {} wins!", self.players[self.turn as usize].symbol);
                    break;
                }
                self.determine_turn();
            }
        }

        fn check_board(&self) -> bool {
            // Check for a winner
            for player in self.players.iter() {
                if self.board.cells[0][0] == player.symbol
                    && self.board.cells[0][1] == player.symbol
                    && self.board.cells[0][2] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[1][0] == player.symbol
                    && self.board.cells[1][1] == player.symbol
                    && self.board.cells[1][2] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[2][0] == player.symbol
                    && self.board.cells[2][1] == player.symbol
                    && self.board.cells[2][2] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[0][0] == player.symbol
                    && self.board.cells[1][0] == player.symbol
                    && self.board.cells[2][0] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[0][1] == player.symbol
                    && self.board.cells[1][1] == player.symbol
                    && self.board.cells[2][1] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[0][2] == player.symbol
                    && self.board.cells[1][2] == player.symbol
                    && self.board.cells[2][2] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[0][0] == player.symbol
                    && self.board.cells[1][1] == player.symbol
                    && self.board.cells[2][2] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                } else if self.board.cells[0][2] == player.symbol
                    && self.board.cells[1][1] == player.symbol
                    && self.board.cells[2][0] == player.symbol
                {
                    println!("Player {} wins!", player.symbol);
                    return true;
                }
            }

            return false;
        }

        fn determine_turn(&mut self) {
            self.turn = (self.turn + 1) % 2;
        }

        fn take_turn(&mut self) {
            println!("Player {}'s turn.", self.players[self.turn as usize].symbol);

            // Ask the user to enter a move
            println!("Enter a column (e.g. A-C): ");
            let mut column = String::new();
            std::io::stdin()
                .read_line(&mut column)
                .expect("Failed to read line.");

            println!("Enter a row (e.g. 1-3): ");
            let mut row = String::new();
            std::io::stdin()
                .read_line(&mut row)
                .expect("Failed to read line.");

            // Convert the column to a number
            let column = match column.trim().to_lowercase().as_ref() {
                "a" => 0,
                "b" => 1,
                "c" => 2,
                "A" => 0,
                "B" => 1,
                "C" => 2,
                _ => {
                    println!("Invalid column.");
                    return;
                }
            };

            // Convert the row to a number
            let row = match row.trim().as_ref() {
                "1" => 0,
                "2" => 1,
                "3" => 2,
                _ => {
                    println!("Invalid row.");
                    return;
                }
            };

            // Check if the cell is empty
            if self.board.cells[row][column] != ' ' {
                println!("Cell is already taken.");
                return;
            }

            // Place the player's symbol in the cell
            self.board.cells[row][column] = self.players[self.turn as usize].symbol;
        }
    }

    impl Player {
        pub fn new(symbol: char) -> Player {
            Player {
                symbol: symbol,
                score: 0,
            }
        }
    }

    impl Board {
        pub fn new() -> Board {
            Board {
                cells: [[' '; 3]; 3],
            }
        }

        pub fn display(&self) {
            // Print the header
            println!("  | A | B | C |");
            println!("--+---+---+---+");

            // Print the rows
            for (i, row) in self.cells.iter().enumerate() {
                // Print the row number
                print!("{} | ", i + 1);

                // Print the cells
                for cell in row.iter() {
                    print!("{} | ", cell);
                }

                // Print the row separator
                if i < 2 {
                    println!("\n--+---+---+---+");
                } else {
                    println!("\n---------------");
                }
            }
        }
    }
}
