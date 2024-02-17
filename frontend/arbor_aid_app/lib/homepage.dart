import 'package:flutter/material.dart';



class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Image.asset(
            'assets/twoMarines.png',
            width: 50,
            height: 50,
          ),
        ),
        actions: [
          IconButton(
            icon: Icon(Icons.menu),
            onPressed: () {
              Scaffold.of(context).openDrawer();
            },
          ),
        ],
      ),
      drawer: Drawer(
        // Populate the Drawer in the next step.
        child: ListView(
          children: <Widget>[
            ListTile(
              title: Text('Data Entry'),
              onTap: () {
                // Update the state of the app.
                Navigator.pushNamed(context, '/dataEntry'); // close the drawer
                // Navigate to the Data Entry page.
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
