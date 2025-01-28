import 'package:flutter/material.dart';

void main() {
  runApp(const MovementGame());
}

class MovementGame extends StatelessWidget {
  const MovementGame({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: GameScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class GameScreen extends StatefulWidget {
  const GameScreen({super.key});

  @override
  _GameScreenState createState() => _GameScreenState();
}

class _GameScreenState extends State<GameScreen> {
  double _xPosition = 960; // Initial X position of the moving image
  double _yPosition = 540; // Initial Y position of the moving image

  void _moveUp() {
    setState(() {
      _yPosition = (_yPosition - 20).clamp(0, double.infinity); // Move up
    });
  }

  void _moveDown() {
    setState(() {
      _yPosition = (_yPosition + 20).clamp(0, 800); // Move down
    });
  }

  void _moveLeft() {
    setState(() {
      _xPosition = (_xPosition - 20).clamp(0, double.infinity); // Move left
    });
  }

  void _moveRight() {
    setState(() {
      _xPosition = (_xPosition + 20).clamp(0, 1500); // Move right
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background Image
          Positioned.fill(
            child: Image.asset(
              './assets/background.png',
              fit: BoxFit.cover,
            ),
          ),
          // Moving Image
          Positioned(
            top: _yPosition,
            left: _xPosition,
            child: Image.asset(
              './assets/player.png',
              width: 50,
              height: 50,
            ),
          ),
          // Arrow Buttons
          Positioned(
            bottom: 50,
            left: 0,
            right: 0,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // Left Arrow
                IconButton(
                  onPressed: _moveLeft,
                  icon: Icon(Icons.arrow_left, size: 50),
                ),
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Up Arrow
                    IconButton(
                      onPressed: _moveUp,
                      icon: Icon(Icons.arrow_drop_up, size: 50),
                    ),
                    // Down Arrow
                    IconButton(
                      onPressed: _moveDown,
                      icon: Icon(Icons.arrow_drop_down, size: 50),
                    ),
                  ],
                ),
                // Right Arrow
                IconButton(
                  onPressed: _moveRight,
                  icon: Icon(Icons.arrow_right, size: 50),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
