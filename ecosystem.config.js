module.exports = {
  apps: [
    {
      name: "price_checker_hub",
      script: "venv/bin/gunicorn",
      args: ["price_checker_hub.wsgi:application", "--bind=0.0.0.0:8001"],
      watch: false,
      ignore_watch: ["static", "media", ".git"],
      interpreter: "./venv/bin/python",
      exec_mode: "fork",
      env: {
        NODE_ENV: "development",
      },
      env_production: {
        NODE_ENV: "production",
      },
    },
  ],
};
