import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: CircleAvatar(
          radius: 80,
          backgroundColor: Colors.transparent,
          backgroundImage: AssetImage('assets/twoMarines.png'),
        ),
        /*
        leading: IconButton(
          icon: Container(
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              image: DecorationImage(
                image: AssetImage('assets/twoMarines.png'),
                fit: BoxFit.cover,
              ),
            ),
            width: 65,
            height: 65,
          ),
          onPressed: () {
            
          },
        ), */
        actions: [
          IconButton(
            icon: Icon(Icons.menu),
            onPressed: () {
              Scaffold.of(context).openDrawer(); // Or other action
            },
          ),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          children: <Widget>[
            ListTile(
              title: Text('Data Entry'),
              onTap: () {
                Navigator.pushNamed(context, '/dataEntry');
              },
            ),
            // Add other ListTile items here
          ],
        ),
      ),
      body: Center(
        child: Text(
          'Home Page Content',
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}
