# frontend/Dockerfile
FROM node:20-alpine AS build

WORKDIR /app

# package.json ve package-lock.json (varsa) kopyala
COPY package*.json ./

# Bağımlılıkları yükle
RUN npm install

# Tüm kaynak kodları kopyala
COPY . .

# Uygulamayı build et
RUN npm run build

# Üretim aşaması
FROM nginx:alpine
# Build aşamasından dist klasörünü kopyala
COPY --from=build /app/dist /usr/share/nginx/html
# Nginx yapılandırmasını kopyala
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
