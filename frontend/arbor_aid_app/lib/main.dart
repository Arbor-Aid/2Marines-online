<<<<<<< HEAD
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
    );
  }
}

Future<void> main() async {
  await dotenv.load(
      fileName: ".env"); // Updated to reflect the new root location
  runApp(const MyApp());
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _selectedIndex = 0;

  static final List<Widget> _widgetOptions = <Widget>[
    const HomeScreen(),
    const Text('Messages Screen'),
    const Text('Notifications Screen'),
    const Text('Settings Screen'),
    const ServiceLocatorScreen(), // Assuming you have this screen set up
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('2Marines App'),
      ),
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.message),
            label: 'Messages',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.notifications),
            label: 'Notifications',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Image.asset(
          'assets/logo.png', // Make sure this file exists in the assets folder
          height: 100,
          width: 100,
        ),
        const SizedBox(height: 32),
        DashboardSection(
          icon: Icons.home,
          title: 'Find Support',
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => const ServiceLocatorScreen()),
            );
          },
        ),
        const SizedBox(height: 16),
        DashboardSection(
          icon: Icons.trending_up,
          title: 'Track Progress',
          onTap: () {
            // Implement navigation to progress tracking screen
          },
        ),
        const SizedBox(height: 16),
        DashboardSection(
          icon: Icons.people,
          title: 'Community Resources',
          onTap: () {
            // Implement navigation to community resources screen
          },
        ),
        const SizedBox(height: 16),
        DashboardSection(
          icon: Icons.person,
          title: 'Profile',
          onTap: () {
            // Implement navigation to profile screen
          },
        ),
        const SizedBox(height: 16),
        // Environment variable usage example
        Text('API URL: ${dotenv.env['OPENAI_API_URL']}'),
      ],
    );
  }
}

class DashboardSection extends StatelessWidget {
  final IconData icon;
  final String title;
  final VoidCallback onTap;

  const DashboardSection({
    super.key,
    required this.icon,
    required this.title,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            children: [
              Icon(icon, size: 48),
              const SizedBox(width: 16),
              Text(
                title,
                style: const TextStyle(fontSize: 18),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class ServiceLocatorScreen extends StatelessWidget {
  const ServiceLocatorScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Service Locator"),
      ),
      body: const Center(
        child: Text("Service Locator Page"),
      ),
=======
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
>>>>>>> 27a9723a0e12c4c078243042e84a5a4b3a137bf8
    );
  }
}
