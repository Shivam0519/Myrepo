# Use Nginx to serve the static website
FROM nginx:alpine AS website

# Set working directory and copy website files
WORKDIR /usr/share/nginx/html
COPY index.html .
COPY styles.css .
COPY script.js .

# Expose port 80 for Nginx
EXPOSE 80
