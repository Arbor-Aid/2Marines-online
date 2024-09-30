import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:your_project/firebase_service.dart'; // Import FirebaseService
import 'login_register_screen.dart'; // Import your login/register screen

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(); // Initialize Firebase
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '2Marines App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const LoginRegisterScreen(), // Change this to your initial screen
    );
  }
}
