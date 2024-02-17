import 'package:arbor_aid_app/homepage.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Arbor Aid App',
      theme: ThemeData(
        // Define the default brightness and colors.
        brightness: Brightness.dark,
        primaryColor: Colors.grey[900],
        
        // Define the default font family.
        fontFamily: 'Montserrat',

        // Define the default `AppBarTheme`.
        appBarTheme: AppBarTheme(
          color: Colors.grey[900],
          iconTheme: IconThemeData(color: Colors.white),
        ), 
      ),
      home: HomePage(),
    );
  }
}

