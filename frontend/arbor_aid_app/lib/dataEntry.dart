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
      ),
      maxLines: maxLines,
    );
  }
}
