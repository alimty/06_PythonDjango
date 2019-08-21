import django_tables2 as tables

from user_account.models.certification import Certification


class CertficationsTable(tables.Table):

    id = tables.TemplateColumn('''
        {% if request.user.is_superuser %}
            <a href="{% url 'admin:user_account_certification_change' record.id %}" target="_blank">
                {{record.id}}
            </a>
        {% else %}
            {{record.id}}
        {% endif %}
        ''', order_by='id')

    user = tables.TemplateColumn('''
        <a href="{% url 'admin-panel-pixuser-edit' record.pixuser.id %}">
        {{ record.pixuser.email }}</a>
        ''', verbose_name="User", orderable=False)

    creation_date = tables.TemplateColumn('{{record.creation_date|date:"d M Y H:i"}}',
                                          verbose_name='Creation date',
                                          order_by='creation_date')

    exam_date = tables.TemplateColumn('{{record.exam_date|date:"d M Y H:i"}}',
                                      verbose_name='Date exam',
                                      order_by='exam_date')

    exam_name = tables.TemplateColumn('Pix4D Fundamentals', orderable=False)

    status = tables.TemplateColumn(
        '{% include "admin_panel/tables/certification/_status_column.html" %}', orderable=False)

    exam_score = tables.Column(verbose_name="Score", orderable=False)

    pdf_path = tables.TemplateColumn('''
        {% if record.pdf_path %}
            <a href="{% url 'user-account-certification-pdf' record.id %}"
            target="_blank">certification PDF</a>
        {% endif %}
        ''', orderable=False, verbose_name='PDF')

    exam_submission_id = tables.Column(verbose_name='Formstack id')
    actions = tables.TemplateColumn('''
        {% load mapper_tags %}
        {% if record.status == 'failed' %}
            <a href="{% url 'admin-panel-certifications-status-succeeded' record.id %}" class="confirm-modal mdl-button mdl-js-button mdl-button--icon" title="Force status succeeded"> <i class="material-icons">done</i>
            </a>
        {% endif %}
        {% if request.user.is_superuser or request.user|has_group:'certification_manager' %}
        <a href="{% url 'admin-panel-certifications-regenerate_pdf' record.id %}"
            class="mdl-button mdl-js-button mdl-button--icon" title="Regenerate PDF Certificate">
              <i class="material-icons">cached</i>
            </a>
        {% endif %}
        ''', orderable=False, verbose_name='Actions')

    class Meta:             # pylint: disable=W0232
        model = Certification
        attrs = {"class": "mdl-data-table mdl-js-data-table"}
        fields = (
            'id', 'user', 'creation_date', 'exam_date', 'exam_name', 'status', 'exam_score',
            'pdf_path', 'exam_submission_id', 'actions'
        )
        order_by = '-id'
