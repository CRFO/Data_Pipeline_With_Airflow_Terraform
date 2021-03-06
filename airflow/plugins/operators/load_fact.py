from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 sql_query="",
                 table="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sql_query = sql_query
        self.table=table
    
    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info(f"Clearing data from Redshift table: {self.table}")
        redshift.run("DELETE FROM {}".format(self.table))
        sql_statement = 'INSERT INTO %s %s' % (self.table, self.sql_query)
        redshift.run(sql_statement)
        self.log.info(sql_statement)
        records = redshift.get_records(f"SELECT COUNT(*) FROM {self.table}")
        self.log.info(f"Total records inserted: {records[0][0]}")
