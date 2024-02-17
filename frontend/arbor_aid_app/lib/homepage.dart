import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _HomePage();
}

class _HomePage extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey,
        leading: IconButton(
          icon: Container(
            decoration: BoxDecoration(
              shape: BoxShape.circle,
            ),
            child: Image.asset(
              'assets/images/C:\Users\dasha\Desktop\2marines\arbor-aid\frontend\arbor_aid_app\Two_Marines_logo.svg',
              // TO DO: sum wrong w this link
              width: 65,
              height: 65,
            ),
          ),
          onPressed: () {
            // Something happens if we press it?
          },
        ),
        actions: [
          IconButton(
            icon: Icon(Icons.menu),
            onPressed: () {
              Scaffold.of(context).openDrawer(); // Or other action
            },
          ),
        ],
      ),
    );
  }
}
