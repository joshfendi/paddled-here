import React, { useEffect, useState } from "react";
import { View, Text, TextInput, Button, StyleSheet, ActivityIndicator } from "react-native";
import { useLocalSearchParams, useRouter } from "expo-router";

export default function editpaddle() {
  const { paddleId } = useLocalSearchParams();
  const router = useRouter();

  const [form, setForm] = useState({
    user_name: "",
    event_name: "",
    location_name: "",
    team: "",
    date: "",
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPaddle = async () => {
      try {
        const res = await fetch(`http://localhost:8000/paddles/${paddleId}`);
        const data = await res.json();
        setForm({
          user_name: data.user_name || "",
          event_name: data.event_name || "",
          location_name: data.location_name || "",
          team: data.team || "",
          date: data.date || "",
        });
      } catch (err) {
        console.error("Error loading paddle:", err);
      } finally {
        setLoading(false);
      }
    };

    if (paddleId) fetchPaddle();
  }, [paddleId]);

  const handleChange = (field: string, value: string) => {
    setForm({ ...form, [field]: value });
  };

  const handleSubmit = async () => {
    try {
      await fetch(`http://localhost:8000/paddles/${paddleId}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });
      router.back(); // go back to previous screen
    } catch (err) {
      console.error("Update failed:", err);
    }
  };

  if (loading) return <ActivityIndicator size="large" style={{ marginTop: 100 }} />;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Edit Paddle Log</Text>
      {["user_name", "event_name", "location_name", "team", "date"].map((field) => (
        <TextInput
          key={field}
          style={styles.input}
          placeholder={field}
          value={form[field as keyof typeof form]}
          onChangeText={(text) => handleChange(field, text)}
        />
      ))}
      <Button title="Update" onPress={handleSubmit} />
      <Button
        title="Delete"
        color="red"
        onPress={async () => {
          try {
            await fetch(`http://localhost:8000/paddles/${paddleId}`, {
              method: "DELETE",
            });
            router.back(); // Go back after successful delete
          } catch (err) {
            console.error("Delete failed:", err);
          }
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, paddingTop: 60, backgroundColor: "#fff" },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 6,
    padding: 10,
    marginBottom: 10,
  },
});
