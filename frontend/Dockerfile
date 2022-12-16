# ==== CONFIGURE =====#
FROM node:lts-slim

ENV NODE_ENV=production

COPY ./frontend/ .

WORKDIR /macros-frontend


# ==== BUILD =====
RUN npm ci

RUN npm run build

# ==== RUN =======
EXPOSE 3000