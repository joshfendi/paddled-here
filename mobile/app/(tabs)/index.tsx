import React, { useEffect, useState } from "react";
import { View, Text, FlatList, StyleSheet } from "react-native";

type PaddleLocation = {
  id: number;
  user_name: string;
  event_name: string;
  location_name: string;
  date: string;
  team?: string // optional field
};

export default function HomeScreen() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [paddles, setPaddles] = useState<PaddleLocation[]>([]);

  useEffect(() => {
    const fetchPaddles = async () => {
      try {
        const res = await fetch("http://localhost:8000/paddles");
        const data = await res.json();
        setPaddles(data.results);
      }
      catch (err) {
        console.error(err);
        setError("Failed to load paddles");
      }
      finally {
        setLoading(false);
      }
    }

    fetchPaddles();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Paddle Logs</Text>
      {loading && <Text>Loading...</Text>}
      {error && <Text style={{ color: "red" }}>{error}</Text>}
      <FlatList
        data={paddles}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.event}>{item.team && <Text>{item.team} | </Text>}{item.event_name}</Text>
            <Text>{item.location_name}</Text>
            <Text>{item.date}</Text>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, paddingTop: 60, backgroundColor: "#fff" },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  card: {
    padding: 10,
    marginBottom: 10,
    backgroundColor: "#f2f2f2",
    borderRadius: 8,
  },
  event: { fontSize: 18, fontWeight: "600" },
});
