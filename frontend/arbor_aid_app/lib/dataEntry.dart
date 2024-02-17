import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: DataEntryPage(),
    );
  }
}

class DataEntryPage extends StatefulWidget {
  @override
  _DataEntryPageState createState() => _DataEntryPageState();
  
}

class _DataEntryPageState extends State<DataEntryPage> {
  bool isAppointmentRequired = false;
  List<bool> isSelected = List.generate(7, (_) => false); // For the days of the week

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Data Entry'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            _buildTextField('Organization Name'),
            SizedBox(height: 10),
            _buildTextField('Description', maxLines: 3),
            SizedBox(height: 10),
            _buildTextField('Services'),
            SizedBox(height: 10),
            _buildTextField('Address'),
            SizedBox(height: 10),
            _buildTextField('Phone Number'),
            SizedBox(height: 10),
            _buildTextField('Email'),
            SizedBox(height: 10),
            _buildTextField('Website URL'),
            SizedBox(height: 20),
            Text('Appointment Required? (Check for yes)'),
            Checkbox(
              value: isAppointmentRequired,
              onChanged: (bool? newValue) {
                setState(() {
                  isAppointmentRequired = newValue!;
                });
              },
            ),
            _buildTextField('Who is this for?'),
            SizedBox(height: 20),
            ToggleButtons(
              borderColor: Colors.transparent,
              fillColor: Colors.lightBlue.shade50,
              selectedBorderColor: Colors.blue,
              selectedColor: Colors.black,
              borderRadius: BorderRadius.circular(30),
              children: <Widget>[
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Mon'),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Tue'),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Wed'),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Thu'),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Fri'),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Sat'),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text('Sun'),
                ),
              ],
              onPressed: (int index) {
                setState(() {
                  isSelected[index] = !isSelected[index];
                });
              },
              isSelected: isSelected,
            ),
            SizedBox(height: 20),
            // Add other UI elements here
          ],
        ),
      ),
    );
  }

  Widget _buildTextField(String label, {int maxLines = 1}) {
    return TextField(
      decoration: InputDecoration(
        labelText: label,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(30.0),
        ),
        filled: true,
        fillColor: Colors.white,
      ),
      style: TextStyle(color: Colors.black),
      maxLines: maxLines,
    );
  }
}
