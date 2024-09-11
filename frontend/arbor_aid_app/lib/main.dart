import 'package:arbor_aid_app/dataEntry.dart';
import 'package:arbor_aid_app/homepage.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Arbor Aid App',
      theme: ThemeData(
        // Define the default brightness and colors.
        brightness: Brightness.dark,
        primaryColor: Colors.grey[900],

        // Define the default font family.
        fontFamily: 'Montserrat',

        // Define the default `AppBarTheme`.
        appBarTheme: AppBarTheme(
          color: Color.fromARGB(255, 232, 232, 232),
          iconTheme: IconThemeData(color: const Color.fromARGB(255, 250, 250, 250)),
        ), 
      ),
      home: HomePage(),
      routes: {
        '/dataEntry': (context) => DataEntryPage(), // Data Entry route
      },
    );
  }
}
