FROM python:3.12-slim
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
 && ln -s /root/.local/bin/uv /usr/local/bin/uv

WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv pip sync pyproject.toml --system

COPY . .
CMD ["uv", "run", "--", "python", "main.py"]
