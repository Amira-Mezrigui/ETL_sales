FROM amancevice/pandas

WORKDIR /sales_project
ADD ./scripts/collect_data.py /sales_project/scripts/collect_data.py
ADD ./schema/schema.sql /sales_project/schema/schema.sql
ADD ./analyse/analyse.sql /sales_project/analyse/analyse.sql

WORKDIR /sales_project/scripts
EXPOSE 4000

CMD python collect_data.py\
    && sleep 10