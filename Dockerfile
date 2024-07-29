FROM amancevice/pandas

WORKDIR /sales_project
ADD ./scripts /sales_project/scripts/
ADD ./schema/schema.sql /sales_project/schema/schema.sql
ADD ./analyse/analyse.sql /sales_project/analyse/analyse.sql

WORKDIR /sales_project/scripts

CMD python collect_data.py \
    && echo "Time to Sleep !!!"\
    && sleep 10
