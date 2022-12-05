# ==== CONFIGURE =====#
FROM node:lts-slim

WORKDIR /macros-frontend

COPY ./frontend/ .

# ==== BUILD =====
RUN npm ci

RUN npm run build

# ==== RUN =======
ENV NODE_ENV=production
EXPOSE 3000
CMD [ "npx", "serve", "build" ]