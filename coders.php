<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AppCoders - توسعه نوآوری</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #4a90e2;
            --secondary: #9b59b6;
            --bg: #ffffff;
            --text: #2c3e50;
            --neon: 0 0 15px var(--primary);
        }

        .dark-theme {
            --bg: #1a1a2e;
            --text: #e6e6e6;
            --neon: 0 0 25px var(--primary);
        }

        * {
            transition: all 0.3s ease;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg);
            color: var(--text);
        }

        .header {
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            text-shadow: var(--neon);
            color: white;
        }

        .theme-toggle {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1.5rem;
            color: white;
        }

        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
            color: white;
        }

        .neon-text {
            text-shadow: 0 0 10px var(--primary),
                         0 0 20px var(--primary),
                         0 0 30px var(--secondary);
            animation: neonGlow 1.5s ease-in-out infinite alternate;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            padding: 4rem 2rem;
        }

        .feature-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid var(--primary);
            box-shadow: var(--neon);
        }

        @keyframes neonGlow {
            from {
                text-shadow: 0 0 10px var(--primary),
                            0 0 20px var(--primary);
            }
            to {
                text-shadow: 0 0 20px var(--primary),
                            0 0 30px var(--primary),
                            0 0 40px var(--secondary);
            }
        }

        .btn {
            padding: 1rem 2rem;
            background: var(--primary);
            border: none;
            border-radius: 25px;
            color: white;
            cursor: pointer;
            box-shadow: var(--neon);
        }

        .btn:hover {
            transform: translateY(-3px);
            background: var(--secondary);
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">AppCoders</div>
        <button class="theme-toggle" id="themeToggle">
            <i class="fas fa-sun"></i>
        </button>
    </header>

    <section class="hero">
        <h1 class="neon-text">به دنیای نوآوری خوش آمدید</h1>
        <p>توسعه دهنده راهکارهای فناوری آینده</p>
        <a href="https://appcoders.ir" class="btn">ورود به دنیای کدنویسی</a>
    </section>

    <section class="features">
        <div class="feature-card">
            <h3>توسعه نرم افزار</h3>
            <p>راهکارهای سفارشی متناسب با نیازهای کسب و کار شما</p>
        </div>
        <div class="feature-card">
            <h3>طراحی رابط کاربری</h3>
            <p>تجربه کاربری بی نظیر با طراحی مدرن و واکنشگرا</p>
        </div>
        <div class="feature-card">
            <h3>مشاوره فناوری</h3>
            <p>ارائه راهکارهای مبتنی بر آخرین تکنولوژی‌های روز</p>
        </div>
    </section>

    <script>
        const themeToggle = document.getElementById('themeToggle');
        const body = document.body;

        themeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-theme');
            themeToggle.innerHTML = body.classList.contains('dark-theme') ? 
                '<i class="fas fa-moon"></i>' : 
                '<i class="fas fa-sun"></i>';
        });
    </script>
</body>
</html>