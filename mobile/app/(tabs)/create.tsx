import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet, ScrollView, Alert } from "react-native";

export default function CreatePaddleScreen() {
  const [form, setForm] = useState({
    user_name: "",
    event_name: "",
    team: "",
    location_name: "",
    lat: "",
    lng: "",
    date: "",
    notes: "",
    photo_url: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (key: string, value: string) => {
    setForm((prev) => ({ ...prev, [key]: value }));
  };

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);

    // Prepare payload
    const payload = {
      ...form,
      coordinates: {
        lat: parseFloat(form.lat),
        lng: parseFloat(form.lng),
      },
    };

    try {
      const res = await fetch("http://localhost:8000/paddles", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();
      Alert.alert("Success", "Paddle log created!");
      setForm({
        user_name: "",
        event_name: "",
        team: "",
        location_name: "",
        lat: "",
        lng: "",
        date: "",
        notes: "",
        photo_url: "",
      });
    } catch (err) {
      console.error("Submit failed:", err);
      setError("Failed to create paddle log");
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Create Paddle Log</Text>

      {error && <Text style={{ color: "red", marginBottom: 10 }}>{error}</Text>}

      <TextInput placeholder="User Name" style={styles.input} value={form.user_name} onChangeText={(text) => handleChange("user_name", text)} />
      <TextInput placeholder="Event Name" style={styles.input} value={form.event_name} onChangeText={(text) => handleChange("event_name", text)} />
      <TextInput placeholder="Team (optional)" style={styles.input} value={form.team} onChangeText={(text) => handleChange("team", text)} />
      <TextInput placeholder="Location Name" style={styles.input} value={form.location_name} onChangeText={(text) => handleChange("location_name", text)} />
      <TextInput placeholder="Latitude" keyboardType="numeric" style={styles.input} value={form.lat} onChangeText={(text) => handleChange("lat", text)} />
      <TextInput placeholder="Longitude" keyboardType="numeric" style={styles.input} value={form.lng} onChangeText={(text) => handleChange("lng", text)} />
      <TextInput placeholder="Date (YYYY-MM-DD)" style={styles.input} value={form.date} onChangeText={(text) => handleChange("date", text)} />
      <TextInput placeholder="Notes (optional)" style={styles.input} value={form.notes} onChangeText={(text) => handleChange("notes", text)} multiline />
      <TextInput placeholder="Photo URL (optional)" style={styles.input} value={form.photo_url} onChangeText={(text) => handleChange("photo_url", text)} />

      <Button title={loading ? "Submitting..." : "Submit Paddle Log"} onPress={handleSubmit} disabled={loading} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: "#fff" },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    padding: 10,
    marginBottom: 12,
    borderRadius: 6,
  },
});
