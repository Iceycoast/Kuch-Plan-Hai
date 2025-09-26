import { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./Login.module.css";


const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleSubmit(e) {
        e.preventDefault();
        setError("");
        setLoading(true);

        try {
            const res = await fetch(`${API_BASE}/auth/login`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({ email, password }),
                });
            const data = await res.json();
            if (!res.ok) throw new Error(data.detail || 'Login Failed');

            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);

            alert('Logged in!');
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }

    }

    return (
        <main className={styles.container}>
            
            <section className={styles.card}>
                <header className={styles.header}>
                    <h1 className={styles.title}>Kuch Plan Hai?</h1>
                    <p className={styles.subtitle}>Sign in to your account</p>
                </header>

                {error && (
                    <div className={styles.error}>
                        <p className={styles.errorText}>{error}</p>
                    </div>
                )}

                <form onSubmit={handleSubmit} className={styles.form}>
                    <div className={styles.field}>
                        <label className={styles.label}>Email</label>
                        <input type="email"
                            placeholder="you@example.com"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className={styles.input}
                            required
                            autoComplete="email"
                        />
                    </div>

                    <div className={styles.field}>
                        <label className={styles.label}>Password</label>
                        <input type="password"
                            placeholder="••••••••"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className={styles.input}
                            required
                            minLength={8}
                            autoComplete="current-password"
                        />
                    </div>

                    <button type="submit" disabled={loading} className={styles.button}>
                        {loading ? 'Signing in...' : 'Sign in'}
                    </button>
                </form>

                <footer className="mt-6 text-center">
                    <Link to="/signup" className={styles.secondaryButton} role="button">
                        Don't have an account? Sign up
                    </Link>
                </footer>
            </section>
        </main>
    );
}