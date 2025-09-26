import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import styles from "./SignUp.module.css";

const API_BASE = import.meta.env.VITE_API_URL

export default function SignUp(){
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate();


    async function handleSubmit(e) {
        e.preventDefault();
        setError("");
        setLoading(true);

        try{
            const   res = await fetch(`${API_BASE}/auth/register`,{
                    method : 'POST',
                    headers : {'Content-Type' : 'application/json'},
                    credentials : 'include',
                    body : JSON.stringify({
                        first_name : firstName,
                        last_name : lastName,
                        email,
                        password
                    }),
            });

            const data = await res.json();
            
            if (!res.ok) throw new Error(data.detail || 'Registration Failed');

            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);

            navigate("/login")

            alert('Account created successfully');
        } catch(err) {
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
                        <p className={styles.subtitle}>Create your account</p>
                </header>

                {error && (
                    <div className={styles.error}>
                        <p className={styles.errorText}>{error}</p>
                    </div>
                )}

                <form onSubmit={handleSubmit} className={styles.form}>
                    <div className={styles.field}>
                        <label className={styles.label}>First Name</label>
                        <input  type="text" 
                                placeholder="First Name"
                                value={firstName}
                                onChange={(e) => setFirstName(e.target.value)}
                                className={styles.input}
                                required
                                minLength={3}
                                autoComplete="given-name"
                        />
                    </div>

                    <div className={styles.field}>
                        <label className={styles.label}>Last Name (optional)</label>
                        <input  type="text"
                                placeholder="Last Name"
                                value={lastName}
                                onChange={(e) => setLastName(e.target.value)}
                                className={styles.input}
                                autoComplete="family-name"
                        />
                    </div>

                    <div  className={styles.field}>
                        <label className={styles.label}>Email</label>
                        <input  type="email"
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
                        <input  type="text"
                                placeholder="8 characters"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className={styles.input}
                                required
                                minLength={8}
                                autoComplete="new-password"
                        />
                    </div>

                    <button type="submit" disabled={loading} className={styles.button}>
                        {loading ? 'Creating account...' : 'Sign up'}
                    </button>
                </form>

                <footer className="mt-6 text-center">
                    <Link to="/login" className={styles.secondaryButton} role="button">
                        Already have an account? Sign in
                    </Link>
                </footer>
            </section>
        </main>
    )

}