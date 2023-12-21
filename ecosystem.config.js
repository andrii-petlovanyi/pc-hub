module.exports = {
  apps: [
    {
      name: "price_checker_hub",
      script: "gunicorn",
      args: "price_checker_hub.wsgi:application",
      watch: true,
      ignore_watch: ["static", "media", ".git"],
      interpreter: "./venv/bin/python",
      exec_mode: "single",
      env: {
        NODE_ENV: "development",
      },
      env_production: {
        NODE_ENV: "production",
      },
    },
  ],
};
