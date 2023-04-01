FROM continuumio/anaconda3

WORKDIR /app

EXPOSE 6000

COPY application ./application
COPY mathtools ./mathtools
COPY environment.yml .

RUN conda env create -f environment.yml --name dev

CMD ["conda", "run", "--no-capture-output", "-n", "dev", \
     "flask", "--app", "application/app", "run", "--host", "0.0.0.0", "--port", "6000"]
