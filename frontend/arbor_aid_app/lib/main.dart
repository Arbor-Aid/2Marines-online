import 'package:flutter/material.dart';
import 'service_locator_screen.dart';  // Import your Service Locator Screen here.
import 'package:flutter_dotenv/flutter_dotenv.dart';  // Import dotenv for env variables

Future<void> main() async {
  // Ensure that all necessary services are initialized before the app starts
  await dotenv.load(fileName: ".env");  // Load .env file for API keys or other env variables
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('2Marines Dashboard'),
        ),
        body: const MyHomePage(),
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _selectedIndex = 0;

  // Removed `const` from _widgetOptions because not all widgets should be `const`
  static final List<Widget> _widgetOptions = <Widget>[
    const HomeScreen(),
    const Text('Messages Screen'),
    const Text('Notifications Screen'),
    const Text('Settings Screen'),
    const ServiceLocatorScreen(),  // Added Service Locator screen, ensure this exists
  ];

  // This method handles changing the selected tab
  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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

// Home Screen widget definition
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Image.asset(
          'assets/logo.png',  // Ensure you have this logo image in your assets folder
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
              MaterialPageRoute(builder: (context) => const ServiceLocatorScreen()),
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
      ],
    );
  }
}

// Dashboard Section Widget
class DashboardSection extends StatelessWidget {
  final IconData icon;
  final String title;
  final VoidCallback onTap;

  const DashboardSection({super.key, 
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

