from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class InfoDeterminant(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'cancer_subject'


class WhoIllness(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'cancer_subject'


class RadiationSideEffects(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'cancer_subject'


class ResultsToRecord(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'cancer_subject'
