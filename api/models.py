from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from salesforce import models

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Opportunity(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    is_deleted = models.BooleanField(
        db_column='IsDeleted', verbose_name='Deleted', sf_read_only=models.READ_ONLY, default=False)
    account = models.ForeignKey('Account', models.DO_NOTHING, db_column='AccountId',
                                verbose_name='Account ID', blank=True, null=True)  # Master Detail Relationship *
    is_private = models.BooleanField(
        db_column='IsPrivate', verbose_name='Private', default=models.DefaultedOnCreate(False))
    name = models.CharField(db_column='Name', max_length=120)
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    stage_name = models.CharField(db_column='StageName', max_length=255, verbose_name='Stage', choices=[('Prospecting', 'Prospecting'), ('Qualification', 'Qualification'), ('Needs Analysis', 'Needs Analysis'), ('Value Proposition', 'Value Proposition'), (
        'Id. Decision Makers', 'Id. Decision Makers'), ('Perception Analysis', 'Perception Analysis'), ('Proposal/Price Quote', 'Proposal/Price Quote'), ('Negotiation/Review', 'Negotiation/Review'), ('Closed Won', 'Closed Won'), ('Closed Lost', 'Closed Lost')])
    amount = models.DecimalField(
        db_column='Amount', max_digits=18, decimal_places=2, blank=True, null=True)
    probability = models.DecimalField(db_column='Probability', max_digits=3, decimal_places=0,
                                      verbose_name='Probability (%)', default=models.DEFAULTED_ON_CREATE, blank=True, null=True)
    expected_revenue = models.DecimalField(db_column='ExpectedRevenue', max_digits=18, decimal_places=2,
                                           verbose_name='Expected Amount', sf_read_only=models.READ_ONLY, blank=True, null=True)
    total_opportunity_quantity = models.DecimalField(
        db_column='TotalOpportunityQuantity', max_digits=18, decimal_places=2, verbose_name='Quantity', blank=True, null=True)
    close_date = models.DateField(db_column='CloseDate')
    type = models.CharField(db_column='Type', max_length=255, verbose_name='Opportunity Type', choices=[('Existing Customer - Upgrade', 'Existing Customer - Upgrade'), (
        'Existing Customer - Replacement', 'Existing Customer - Replacement'), ('Existing Customer - Downgrade', 'Existing Customer - Downgrade'), ('New Customer', 'New Customer')], blank=True, null=True)
    next_step = models.CharField(
        db_column='NextStep', max_length=255, blank=True, null=True)
    lead_source = models.CharField(db_column='LeadSource', max_length=255, choices=[('Web', 'Web'), ('Phone Inquiry', 'Phone Inquiry'), (
        'Partner Referral', 'Partner Referral'), ('Purchased List', 'Purchased List'), ('Other', 'Other')], blank=True, null=True)
    is_closed = models.BooleanField(
        db_column='IsClosed', verbose_name='Closed', sf_read_only=models.READ_ONLY, default=False)
    is_won = models.BooleanField(
        db_column='IsWon', verbose_name='Won', sf_read_only=models.READ_ONLY, default=False)
    forecast_category = models.CharField(db_column='ForecastCategory', max_length=40, sf_read_only=models.READ_ONLY, choices=[(
        'Omitted', 'Omitted'), ('Pipeline', 'Pipeline'), ('BestCase', 'Best Case'), ('MostLikely', 'Most Likely'), ('Forecast', 'Commit'), ('Closed', 'Closed')])
    forecast_category_name = models.CharField(db_column='ForecastCategoryName', max_length=255, verbose_name='Forecast Category', default=models.DEFAULTED_ON_CREATE, choices=[
                                              ('Omitted', 'Omitted'), ('Pipeline', 'Pipeline'), ('Best Case', 'Best Case'), ('Commit', 'Commit'), ('Closed', 'Closed')], blank=True, null=True)
    campaign_id = models.CharField(db_column='CampaignId', max_length=18, verbose_name='Campaign ID',
                                   blank=True, null=True)  # References to missing tables: ['-Campaign']
    has_opportunity_line_item = models.BooleanField(
        db_column='HasOpportunityLineItem', verbose_name='Has Line Item', sf_read_only=models.READ_ONLY, default=False)
    pricebook2_id = models.CharField(db_column='Pricebook2Id', max_length=18, verbose_name='Price Book ID',
                                     default=models.DEFAULTED_ON_CREATE, blank=True, null=True)  # References to missing tables: ['-Pricebook2']
    owner = models.ForeignKey('User', models.DO_NOTHING, db_column='OwnerId',
                              related_name='opportunity_owner_set', verbose_name='Owner ID', default=models.DEFAULTED_ON_CREATE)
    created_date = models.DateTimeField(
        db_column='CreatedDate', sf_read_only=models.READ_ONLY)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='CreatedById',
                                   related_name='opportunity_createdby_set', verbose_name='Created By ID', sf_read_only=models.READ_ONLY)
    last_modified_date = models.DateTimeField(
        db_column='LastModifiedDate', sf_read_only=models.READ_ONLY)
    last_modified_by = models.ForeignKey('User', models.DO_NOTHING, db_column='LastModifiedById',
                                         related_name='opportunity_lastmodifiedby_set', verbose_name='Last Modified By ID', sf_read_only=models.READ_ONLY)
    system_modstamp = models.DateTimeField(
        db_column='SystemModstamp', sf_read_only=models.READ_ONLY)
    last_activity_date = models.DateField(
        db_column='LastActivityDate', verbose_name='Last Activity', sf_read_only=models.READ_ONLY, blank=True, null=True)
    push_count = models.IntegerField(
        db_column='PushCount', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_stage_change_date = models.DateTimeField(
        db_column='LastStageChangeDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    fiscal_quarter = models.IntegerField(
        db_column='FiscalQuarter', sf_read_only=models.READ_ONLY, blank=True, null=True)
    fiscal_year = models.IntegerField(
        db_column='FiscalYear', sf_read_only=models.READ_ONLY, blank=True, null=True)
    fiscal = models.CharField(db_column='Fiscal', max_length=6, verbose_name='Fiscal Period',
                              sf_read_only=models.READ_ONLY, blank=True, null=True)
    contact_id = models.CharField(db_column='ContactId', max_length=18, verbose_name='Contact ID',
                                  sf_read_only=models.NOT_UPDATEABLE, blank=True, null=True)  # References to missing tables: ['-Contact']
    last_viewed_date = models.DateTimeField(
        db_column='LastViewedDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_referenced_date = models.DateTimeField(
        db_column='LastReferencedDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    has_open_activity = models.BooleanField(
        db_column='HasOpenActivity', sf_read_only=models.READ_ONLY, default=False)
    has_overdue_task = models.BooleanField(
        db_column='HasOverdueTask', sf_read_only=models.READ_ONLY, default=False)
    last_amount_changed_history_id = models.CharField(db_column='LastAmountChangedHistoryId', max_length=18, verbose_name='Opportunity History ID',
                                                      sf_read_only=models.READ_ONLY, blank=True, null=True)  # References to missing tables: ['-OpportunityHistory']
    last_close_date_changed_history_id = models.CharField(db_column='LastCloseDateChangedHistoryId', max_length=18, verbose_name='Opportunity History ID',
                                                          sf_read_only=models.READ_ONLY, blank=True, null=True)  # References to missing tables: ['-OpportunityHistory']
    delivery_installation_status = models.CharField(db_column='DeliveryInstallationStatus__c', max_length=255, verbose_name='Delivery/Installation Status', choices=[
                                                    ('In progress', 'In progress'), ('Yet to begin', 'Yet to begin'), ('Completed', 'Completed')], blank=True, null=True)
    tracking_number = models.CharField(
        db_column='TrackingNumber__c', max_length=12, blank=True, null=True)
    order_number = models.CharField(
        db_column='OrderNumber__c', max_length=8, blank=True, null=True)
    current_generators = models.CharField(
        db_column='CurrentGenerators__c', max_length=100, verbose_name='Current Generator(s)', blank=True, null=True)
    main_competitors = models.CharField(
        db_column='MainCompetitors__c', max_length=100, verbose_name='Main Competitor(s)', blank=True, null=True)

    class Meta(models.Model.Meta):
        db_table = 'Opportunity'
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunities'
        # keyPrefix = '006'


class Account(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    is_deleted = models.BooleanField(
        db_column='IsDeleted', verbose_name='Deleted', sf_read_only=models.READ_ONLY, default=False)
    master_record = models.ForeignKey('self', models.DO_NOTHING, db_column='MasterRecordId', related_name='account_masterrecord_set',
                                      verbose_name='Master Record ID', sf_read_only=models.READ_ONLY, blank=True, null=True)
    name = models.CharField(
        db_column='Name', max_length=255, verbose_name='Account Name')
    type = models.CharField(db_column='Type', max_length=255, verbose_name='Account Type', choices=[('Prospect', 'Prospect'), ('Customer - Direct', 'Customer - Direct'), ('Customer - Channel', 'Customer - Channel'), (
        'Channel Partner / Reseller', 'Channel Partner / Reseller'), ('Installation Partner', 'Installation Partner'), ('Technology Partner', 'Technology Partner'), ('Other', 'Other')], blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId',
                               related_name='account_parent_set', verbose_name='Parent Account ID', blank=True, null=True)
    billing_street = models.TextField(
        db_column='BillingStreet', blank=True, null=True)
    billing_city = models.CharField(
        db_column='BillingCity', max_length=40, blank=True, null=True)
    billing_state = models.CharField(
        db_column='BillingState', max_length=80, verbose_name='Billing State/Province', blank=True, null=True)
    billing_postal_code = models.CharField(
        db_column='BillingPostalCode', max_length=20, verbose_name='Billing Zip/Postal Code', blank=True, null=True)
    billing_country = models.CharField(
        db_column='BillingCountry', max_length=80, blank=True, null=True)
    billing_latitude = models.DecimalField(
        db_column='BillingLatitude', max_digits=18, decimal_places=15, blank=True, null=True)
    billing_longitude = models.DecimalField(
        db_column='BillingLongitude', max_digits=18, decimal_places=15, blank=True, null=True)
    billing_geocode_accuracy = models.CharField(db_column='BillingGeocodeAccuracy', max_length=40, choices=[('Address', 'Address'), ('NearAddress', 'NearAddress'), ('Block', 'Block'), ('Street', 'Street'), (
        'ExtendedZip', 'ExtendedZip'), ('Zip', 'Zip'), ('Neighborhood', 'Neighborhood'), ('City', 'City'), ('County', 'County'), ('State', 'State'), ('Unknown', 'Unknown')], blank=True, null=True)
    # This field type is a guess.
    billing_address = models.TextField(
        db_column='BillingAddress', sf_read_only=models.READ_ONLY, blank=True, null=True)
    shipping_street = models.TextField(
        db_column='ShippingStreet', blank=True, null=True)
    shipping_city = models.CharField(
        db_column='ShippingCity', max_length=40, blank=True, null=True)
    shipping_state = models.CharField(
        db_column='ShippingState', max_length=80, verbose_name='Shipping State/Province', blank=True, null=True)
    shipping_postal_code = models.CharField(
        db_column='ShippingPostalCode', max_length=20, verbose_name='Shipping Zip/Postal Code', blank=True, null=True)
    shipping_country = models.CharField(
        db_column='ShippingCountry', max_length=80, blank=True, null=True)
    shipping_latitude = models.DecimalField(
        db_column='ShippingLatitude', max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_longitude = models.DecimalField(
        db_column='ShippingLongitude', max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_geocode_accuracy = models.CharField(db_column='ShippingGeocodeAccuracy', max_length=40, choices=[('Address', 'Address'), ('NearAddress', 'NearAddress'), ('Block', 'Block'), ('Street', 'Street'), (
        'ExtendedZip', 'ExtendedZip'), ('Zip', 'Zip'), ('Neighborhood', 'Neighborhood'), ('City', 'City'), ('County', 'County'), ('State', 'State'), ('Unknown', 'Unknown')], blank=True, null=True)
    # This field type is a guess.
    shipping_address = models.TextField(
        db_column='ShippingAddress', sf_read_only=models.READ_ONLY, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=40,
                             verbose_name='Account Phone', blank=True, null=True)
    fax = models.CharField(db_column='Fax', max_length=40,
                           verbose_name='Account Fax', blank=True, null=True)
    account_number = models.CharField(
        db_column='AccountNumber', max_length=40, blank=True, null=True)
    website = models.URLField(db_column='Website', blank=True, null=True)
    photo_url = models.URLField(db_column='PhotoUrl', verbose_name='Photo URL',
                                sf_read_only=models.READ_ONLY, blank=True, null=True)
    sic = models.CharField(db_column='Sic', max_length=20,
                           verbose_name='SIC Code', blank=True, null=True)
    industry = models.CharField(db_column='Industry', max_length=255, choices=[('Agriculture', 'Agriculture'), ('Apparel', 'Apparel'), ('Banking', 'Banking'), ('Biotechnology', 'Biotechnology'), ('Chemicals', 'Chemicals'), ('Communications', 'Communications'), ('Construction', 'Construction'), ('Consulting', 'Consulting'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'), ('Engineering', 'Engineering'), ('Entertainment', 'Entertainment'), ('Environmental', 'Environmental'), ('Finance', 'Finance'), (
        'Food & Beverage', 'Food & Beverage'), ('Government', 'Government'), ('Healthcare', 'Healthcare'), ('Hospitality', 'Hospitality'), ('Insurance', 'Insurance'), ('Machinery', 'Machinery'), ('Manufacturing', 'Manufacturing'), ('Media', 'Media'), ('Not For Profit', 'Not For Profit'), ('Recreation', 'Recreation'), ('Retail', 'Retail'), ('Shipping', 'Shipping'), ('Technology', 'Technology'), ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Utilities', 'Utilities'), ('Other', 'Other')], blank=True, null=True)
    annual_revenue = models.DecimalField(
        db_column='AnnualRevenue', max_digits=18, decimal_places=0, blank=True, null=True)
    number_of_employees = models.IntegerField(
        db_column='NumberOfEmployees', verbose_name='Employees', blank=True, null=True)
    ownership = models.CharField(db_column='Ownership', max_length=255, choices=[('Public', 'Public'), (
        'Private', 'Private'), ('Subsidiary', 'Subsidiary'), ('Other', 'Other')], blank=True, null=True)
    ticker_symbol = models.CharField(
        db_column='TickerSymbol', max_length=20, blank=True, null=True)
    description = models.TextField(
        db_column='Description', verbose_name='Account Description', blank=True, null=True)
    rating = models.CharField(db_column='Rating', max_length=255, verbose_name='Account Rating', choices=[
                              ('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], blank=True, null=True)
    site = models.CharField(db_column='Site', max_length=80,
                            verbose_name='Account Site', blank=True, null=True)
    owner = models.ForeignKey('User', models.DO_NOTHING, db_column='OwnerId',
                              related_name='account_owner_set', verbose_name='Owner ID', default=models.DEFAULTED_ON_CREATE)
    created_date = models.DateTimeField(
        db_column='CreatedDate', sf_read_only=models.READ_ONLY)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='CreatedById',
                                   related_name='account_createdby_set', verbose_name='Created By ID', sf_read_only=models.READ_ONLY)
    last_modified_date = models.DateTimeField(
        db_column='LastModifiedDate', sf_read_only=models.READ_ONLY)
    last_modified_by = models.ForeignKey('User', models.DO_NOTHING, db_column='LastModifiedById',
                                         related_name='account_lastmodifiedby_set', verbose_name='Last Modified By ID', sf_read_only=models.READ_ONLY)
    system_modstamp = models.DateTimeField(
        db_column='SystemModstamp', sf_read_only=models.READ_ONLY)
    last_activity_date = models.DateField(
        db_column='LastActivityDate', verbose_name='Last Activity', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_viewed_date = models.DateTimeField(
        db_column='LastViewedDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_referenced_date = models.DateTimeField(
        db_column='LastReferencedDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    jigsaw = models.CharField(db_column='Jigsaw', max_length=20,
                              verbose_name='Data.com Key', blank=True, null=True)
    jigsaw_company_id = models.CharField(db_column='JigsawCompanyId', max_length=20,
                                         verbose_name='Jigsaw Company ID', sf_read_only=models.READ_ONLY, blank=True, null=True)
    clean_status = models.CharField(db_column='CleanStatus', max_length=40, choices=[('Matched', 'In Sync'), ('Different', 'Different'), ('Acknowledged', 'Reviewed'), (
        'NotFound', 'Not Found'), ('Inactive', 'Inactive'), ('Pending', 'Not Compared'), ('SelectMatch', 'Select Match'), ('Skipped', 'Skipped')], blank=True, null=True)
    account_source = models.CharField(db_column='AccountSource', max_length=255, choices=[('Web', 'Web'), ('Phone Inquiry', 'Phone Inquiry'), (
        'Partner Referral', 'Partner Referral'), ('Purchased List', 'Purchased List'), ('Other', 'Other')], blank=True, null=True)
    duns_number = models.CharField(
        db_column='DunsNumber', max_length=9, verbose_name='D-U-N-S Number', blank=True, null=True)
    tradestyle = models.CharField(
        db_column='Tradestyle', max_length=255, blank=True, null=True)
    naics_code = models.CharField(
        db_column='NaicsCode', max_length=8, verbose_name='NAICS Code', blank=True, null=True)
    naics_desc = models.CharField(db_column='NaicsDesc', max_length=120,
                                  verbose_name='NAICS Description', blank=True, null=True)
    year_started = models.CharField(
        db_column='YearStarted', max_length=4, blank=True, null=True)
    sic_desc = models.CharField(db_column='SicDesc', max_length=80,
                                verbose_name='SIC Description', blank=True, null=True)
    # References to missing tables: ['-DandBCompany']
    dandb_company_id = models.CharField(
        db_column='DandbCompanyId', max_length=18, verbose_name='D&B Company ID', blank=True, null=True)
    # References to missing tables: ['-OperatingHours']
    operating_hours_id = models.CharField(
        db_column='OperatingHoursId', max_length=18, verbose_name='Operating Hour ID', blank=True, null=True)
    customer_priority = models.CharField(db_column='CustomerPriority__c', max_length=255, choices=[
                                         ('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], blank=True, null=True)
    sla = models.CharField(db_column='SLA__c', max_length=255, verbose_name='SLA', choices=[(
        'Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Bronze', 'Bronze')], blank=True, null=True)
    active = models.CharField(db_column='Active__c', max_length=255, choices=[
                              ('No', 'No'), ('Yes', 'Yes')], blank=True, null=True)
    numberof_locations = models.DecimalField(db_column='NumberofLocations__c', max_digits=3,
                                             decimal_places=0, verbose_name='Number of Locations', blank=True, null=True)
    upsell_opportunity = models.CharField(db_column='UpsellOpportunity__c', max_length=255, choices=[
                                          ('Maybe', 'Maybe'), ('No', 'No'), ('Yes', 'Yes')], blank=True, null=True)
    slaserial_number = models.CharField(
        db_column='SLASerialNumber__c', max_length=10, verbose_name='SLA Serial Number', blank=True, null=True)
    slaexpiration_date = models.DateField(
        db_column='SLAExpirationDate__c', verbose_name='SLA Expiration Date', blank=True, null=True)

    class Meta(models.Model.Meta):
        db_table = 'Account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        # keyPrefix = '001'


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(
        db_column='Username', max_length=80)
    last_name = models.CharField(db_column='LastName', max_length=80)
    first_name = models.CharField(
        db_column='FirstName', max_length=40, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=121,
                            verbose_name='Full Name', sf_read_only=models.READ_ONLY)
    company_name = models.CharField(
        db_column='CompanyName', max_length=80, blank=True, null=True)
    division = models.CharField(
        db_column='Division', max_length=80, blank=True, null=True)
    department = models.CharField(
        db_column='Department', max_length=80, blank=True, null=True)
    title = models.CharField(
        db_column='Title', max_length=80, blank=True, null=True)
    street = models.TextField(db_column='Street', blank=True, null=True)
    city = models.CharField(
        db_column='City', max_length=40, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=80,
                             verbose_name='State/Province', blank=True, null=True)
    postal_code = models.CharField(
        db_column='PostalCode', max_length=20, verbose_name='Zip/Postal Code', blank=True, null=True)
    country = models.CharField(
        db_column='Country', max_length=80, blank=True, null=True)
    latitude = models.DecimalField(
        db_column='Latitude', max_digits=18, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(
        db_column='Longitude', max_digits=18, decimal_places=15, blank=True, null=True)
    geocode_accuracy = models.CharField(db_column='GeocodeAccuracy', max_length=40, choices=[('Address', 'Address'), ('NearAddress', 'NearAddress'), ('Block', 'Block'), ('Street', 'Street'), (
        'ExtendedZip', 'ExtendedZip'), ('Zip', 'Zip'), ('Neighborhood', 'Neighborhood'), ('City', 'City'), ('County', 'County'), ('State', 'State'), ('Unknown', 'Unknown')], blank=True, null=True)
    # This field type is a guess.
    address = models.TextField(
        db_column='Address', sf_read_only=models.READ_ONLY, blank=True, null=True)
    email = models.EmailField(db_column='Email')
    email_preferences_auto_bcc = models.BooleanField(
        db_column='EmailPreferencesAutoBcc', verbose_name='AutoBcc')
    email_preferences_auto_bcc_stay_in_touch = models.BooleanField(
        db_column='EmailPreferencesAutoBccStayInTouch', verbose_name='AutoBccStayInTouch')
    email_preferences_stay_in_touch_reminder = models.BooleanField(
        db_column='EmailPreferencesStayInTouchReminder', verbose_name='StayInTouchReminder')
    sender_email = models.EmailField(
        db_column='SenderEmail', verbose_name='Email Sender Address', blank=True, null=True)
    sender_name = models.CharField(
        db_column='SenderName', max_length=80, verbose_name='Email Sender Name', blank=True, null=True)
    signature = models.TextField(
        db_column='Signature', verbose_name='Email Signature', blank=True, null=True)
    stay_in_touch_subject = models.CharField(
        db_column='StayInTouchSubject', max_length=80, verbose_name='Stay-in-Touch Email Subject', blank=True, null=True)
    stay_in_touch_signature = models.TextField(
        db_column='StayInTouchSignature', verbose_name='Stay-in-Touch Email Signature', blank=True, null=True)
    stay_in_touch_note = models.CharField(
        db_column='StayInTouchNote', max_length=512, verbose_name='Stay-in-Touch Email Note', blank=True, null=True)
    phone = models.CharField(
        db_column='Phone', max_length=40, blank=True, null=True)
    fax = models.CharField(
        db_column='Fax', max_length=40, blank=True, null=True)
    mobile_phone = models.CharField(
        db_column='MobilePhone', max_length=40, verbose_name='Mobile', blank=True, null=True)
    alias = models.CharField(db_column='Alias', max_length=8)
    community_nickname = models.CharField(
        db_column='CommunityNickname', max_length=40, verbose_name='Nickname')
    badge_text = models.CharField(db_column='BadgeText', max_length=80,
                                  verbose_name='User Photo badge text overlay', sf_read_only=models.READ_ONLY, blank=True, null=True)
    is_active = models.BooleanField(
        db_column='IsActive', verbose_name='Active', default=models.DefaultedOnCreate(False))
    time_zone_sid_key = models.CharField(
        db_column='TimeZoneSidKey', max_length=40, verbose_name='Time Zone')  # Too long choices skipped
    # References to missing tables: ['-UserRole']
    user_role_id = models.CharField(
        db_column='UserRoleId', max_length=18, verbose_name='Role ID', blank=True, null=True)
    locale_sid_key = models.CharField(
        db_column='LocaleSidKey', max_length=40, verbose_name='Locale')  # Too long choices skipped
    receives_info_emails = models.BooleanField(
        db_column='ReceivesInfoEmails', verbose_name='Info Emails', default=models.DefaultedOnCreate(False))
    receives_admin_info_emails = models.BooleanField(
        db_column='ReceivesAdminInfoEmails', verbose_name='Admin Info Emails', default=models.DefaultedOnCreate(False))
    email_encoding_key = models.CharField(db_column='EmailEncodingKey', max_length=40, verbose_name='Email Encoding', choices=[('UTF-8', 'Unicode (UTF-8)'), ('ISO-8859-1', 'General US & Western Europe (ISO-8859-1, ISO-LATIN-1)'), ('Shift_JIS', 'Japanese (Shift-JIS)'), ('ISO-2022-JP', 'Japanese (JIS)'), (
        'EUC-JP', 'Japanese (EUC)'), ('ks_c_5601-1987', 'Korean (ks_c_5601-1987)'), ('Big5', 'Traditional Chinese (Big5)'), ('GB2312', 'Simplified Chinese (GB2312)'), ('Big5-HKSCS', 'Traditional Chinese Hong Kong (Big5-HKSCS)'), ('x-SJIS_0213', 'Japanese (Shift-JIS_2004)')])
    # References to missing tables: ['-Profile']
    profile_id = models.CharField(
        db_column='ProfileId', max_length=18, verbose_name='Profile ID')
    user_type = models.CharField(db_column='UserType', max_length=40, sf_read_only=models.READ_ONLY, choices=[('Standard', 'Standard'), ('PowerPartner', 'Partner'), ('PowerCustomerSuccess', 'Customer Portal Manager'), (
        'CustomerSuccess', 'Customer Portal User'), ('Guest', 'Guest'), ('CspLitePortal', 'High Volume Portal'), ('CsnOnly', 'CSN Only'), ('SelfService', 'Self Service')], blank=True, null=True)
    language_locale_key = models.CharField(db_column='LanguageLocaleKey', max_length=40, verbose_name='Language', choices=[('en_US', 'English'), ('de', 'German'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('ja', 'Japanese'), ('sv', 'Swedish'), (
        'ko', 'Korean'), ('zh_TW', 'Chinese (Traditional)'), ('zh_CN', 'Chinese (Simplified)'), ('pt_BR', 'Portuguese (Brazil)'), ('nl_NL', 'Dutch'), ('da', 'Danish'), ('th', 'Thai'), ('fi', 'Finnish'), ('ru', 'Russian'), ('es_MX', 'Spanish (Mexico)'), ('no', 'Norwegian')])
    employee_number = models.CharField(
        db_column='EmployeeNumber', max_length=20, blank=True, null=True)
    delegated_approver = models.ForeignKey('self', models.DO_NOTHING, db_column='DelegatedApproverId', related_name='user_delegatedapprover_set',
                                           verbose_name='Delegated Approver ID', blank=True, null=True)  # Reference to tables [User, -Group]
    manager = models.ForeignKey('self', models.DO_NOTHING, db_column='ManagerId',
                                related_name='user_manager_set', verbose_name='Manager ID', blank=True, null=True)
    last_login_date = models.DateTimeField(
        db_column='LastLoginDate', verbose_name='Last Login', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_password_change_date = models.DateTimeField(
        db_column='LastPasswordChangeDate', verbose_name='Last Password Change or Reset', sf_read_only=models.READ_ONLY, blank=True, null=True)
    created_date = models.DateTimeField(
        db_column='CreatedDate', sf_read_only=models.READ_ONLY)
    created_by = models.ForeignKey('self', models.DO_NOTHING, db_column='CreatedById',
                                   related_name='user_createdby_set', verbose_name='Created By ID', sf_read_only=models.READ_ONLY)
    last_modified_date = models.DateTimeField(
        db_column='LastModifiedDate', sf_read_only=models.READ_ONLY)
    last_modified_by = models.ForeignKey('self', models.DO_NOTHING, db_column='LastModifiedById',
                                         related_name='user_lastmodifiedby_set', verbose_name='Last Modified By ID', sf_read_only=models.READ_ONLY)
    system_modstamp = models.DateTimeField(
        db_column='SystemModstamp', sf_read_only=models.READ_ONLY)
    number_of_failed_logins = models.IntegerField(
        db_column='NumberOfFailedLogins', verbose_name='Failed Login Attempts', sf_read_only=models.READ_ONLY, blank=True, null=True)
    offline_trial_expiration_date = models.DateTimeField(
        db_column='OfflineTrialExpirationDate', verbose_name='Offline Edition Trial Expiration Date', sf_read_only=models.READ_ONLY, blank=True, null=True)
    offline_pda_trial_expiration_date = models.DateTimeField(
        db_column='OfflinePdaTrialExpirationDate', verbose_name='Sales Anywhere Trial Expiration Date', sf_read_only=models.READ_ONLY, blank=True, null=True)
    user_permissions_marketing_user = models.BooleanField(
        db_column='UserPermissionsMarketingUser', verbose_name='Marketing User')
    user_permissions_offline_user = models.BooleanField(
        db_column='UserPermissionsOfflineUser', verbose_name='Offline User')
    user_permissions_call_center_auto_login = models.BooleanField(
        db_column='UserPermissionsCallCenterAutoLogin', verbose_name='Auto-login To Call Center')
    user_permissions_sfcontent_user = models.BooleanField(
        db_column='UserPermissionsSFContentUser', verbose_name='Salesforce CRM Content User')
    user_permissions_knowledge_user = models.BooleanField(
        db_column='UserPermissionsKnowledgeUser', verbose_name='Knowledge User')
    user_permissions_interaction_user = models.BooleanField(
        db_column='UserPermissionsInteractionUser', verbose_name='Flow User')
    user_permissions_support_user = models.BooleanField(
        db_column='UserPermissionsSupportUser', verbose_name='Service Cloud User')
    user_permissions_jigsaw_prospecting_user = models.BooleanField(
        db_column='UserPermissionsJigsawProspectingUser', verbose_name='Data.com User')
    user_permissions_siteforce_contributor_user = models.BooleanField(
        db_column='UserPermissionsSiteforceContributorUser', verbose_name='Site.com Contributor User')
    user_permissions_siteforce_publisher_user = models.BooleanField(
        db_column='UserPermissionsSiteforcePublisherUser', verbose_name='Site.com Publisher User')
    user_permissions_work_dot_com_user_feature = models.BooleanField(
        db_column='UserPermissionsWorkDotComUserFeature', verbose_name='WDC User')
    forecast_enabled = models.BooleanField(
        db_column='ForecastEnabled', verbose_name='Allow Forecasting', default=models.DefaultedOnCreate(False))
    user_preferences_activity_reminders_popup = models.BooleanField(
        db_column='UserPreferencesActivityRemindersPopup', verbose_name='ActivityRemindersPopup')
    user_preferences_event_reminders_checkbox_default = models.BooleanField(
        db_column='UserPreferencesEventRemindersCheckboxDefault', verbose_name='EventRemindersCheckboxDefault')
    user_preferences_task_reminders_checkbox_default = models.BooleanField(
        db_column='UserPreferencesTaskRemindersCheckboxDefault', verbose_name='TaskRemindersCheckboxDefault')
    user_preferences_reminder_sound_off = models.BooleanField(
        db_column='UserPreferencesReminderSoundOff', verbose_name='ReminderSoundOff')
    user_preferences_disable_all_feeds_email = models.BooleanField(
        db_column='UserPreferencesDisableAllFeedsEmail', verbose_name='DisableAllFeedsEmail')
    user_preferences_disable_followers_email = models.BooleanField(
        db_column='UserPreferencesDisableFollowersEmail', verbose_name='DisableFollowersEmail')
    user_preferences_disable_profile_post_email = models.BooleanField(
        db_column='UserPreferencesDisableProfilePostEmail', verbose_name='DisableProfilePostEmail')
    user_preferences_disable_change_comment_email = models.BooleanField(
        db_column='UserPreferencesDisableChangeCommentEmail', verbose_name='DisableChangeCommentEmail')
    user_preferences_disable_later_comment_email = models.BooleanField(
        db_column='UserPreferencesDisableLaterCommentEmail', verbose_name='DisableLaterCommentEmail')
    user_preferences_dis_prof_post_comment_email = models.BooleanField(
        db_column='UserPreferencesDisProfPostCommentEmail', verbose_name='DisProfPostCommentEmail')
    user_preferences_content_no_email = models.BooleanField(
        db_column='UserPreferencesContentNoEmail', verbose_name='ContentNoEmail')
    user_preferences_content_email_as_and_when = models.BooleanField(
        db_column='UserPreferencesContentEmailAsAndWhen', verbose_name='ContentEmailAsAndWhen')
    user_preferences_apex_pages_developer_mode = models.BooleanField(
        db_column='UserPreferencesApexPagesDeveloperMode', verbose_name='ApexPagesDeveloperMode')
    user_preferences_receive_no_notifications_as_approver = models.BooleanField(
        db_column='UserPreferencesReceiveNoNotificationsAsApprover', verbose_name='ReceiveNoNotificationsAsApprover')
    user_preferences_receive_notifications_as_delegated_approver = models.BooleanField(
        db_column='UserPreferencesReceiveNotificationsAsDelegatedApprover', verbose_name='ReceiveNotificationsAsDelegatedApprover')
    user_preferences_hide_csnget_chatter_mobile_task = models.BooleanField(
        db_column='UserPreferencesHideCSNGetChatterMobileTask', verbose_name='HideCSNGetChatterMobileTask')
    user_preferences_disable_mentions_post_email = models.BooleanField(
        db_column='UserPreferencesDisableMentionsPostEmail', verbose_name='DisableMentionsPostEmail')
    user_preferences_dis_mentions_comment_email = models.BooleanField(
        db_column='UserPreferencesDisMentionsCommentEmail', verbose_name='DisMentionsCommentEmail')
    user_preferences_hide_csndesktop_task = models.BooleanField(
        db_column='UserPreferencesHideCSNDesktopTask', verbose_name='HideCSNDesktopTask')
    user_preferences_hide_chatter_onboarding_splash = models.BooleanField(
        db_column='UserPreferencesHideChatterOnboardingSplash', verbose_name='HideChatterOnboardingSplash')
    user_preferences_hide_second_chatter_onboarding_splash = models.BooleanField(
        db_column='UserPreferencesHideSecondChatterOnboardingSplash', verbose_name='HideSecondChatterOnboardingSplash')
    user_preferences_dis_comment_after_like_email = models.BooleanField(
        db_column='UserPreferencesDisCommentAfterLikeEmail', verbose_name='DisCommentAfterLikeEmail')
    user_preferences_disable_like_email = models.BooleanField(
        db_column='UserPreferencesDisableLikeEmail', verbose_name='DisableLikeEmail')
    user_preferences_sort_feed_by_comment = models.BooleanField(
        db_column='UserPreferencesSortFeedByComment', verbose_name='SortFeedByComment')
    user_preferences_disable_message_email = models.BooleanField(
        db_column='UserPreferencesDisableMessageEmail', verbose_name='DisableMessageEmail')
    user_preferences_hide_legacy_retirement_modal = models.BooleanField(
        db_column='UserPreferencesHideLegacyRetirementModal', verbose_name='HideLegacyRetirementModal')
    user_preferences_jigsaw_list_user = models.BooleanField(
        db_column='UserPreferencesJigsawListUser', verbose_name='JigsawListUser')
    user_preferences_disable_bookmark_email = models.BooleanField(
        db_column='UserPreferencesDisableBookmarkEmail', verbose_name='DisableBookmarkEmail')
    user_preferences_disable_share_post_email = models.BooleanField(
        db_column='UserPreferencesDisableSharePostEmail', verbose_name='DisableSharePostEmail')
    user_preferences_enable_auto_sub_for_feeds = models.BooleanField(
        db_column='UserPreferencesEnableAutoSubForFeeds', verbose_name='EnableAutoSubForFeeds')
    user_preferences_disable_file_share_notifications_for_api = models.BooleanField(
        db_column='UserPreferencesDisableFileShareNotificationsForApi', verbose_name='DisableFileShareNotificationsForApi')
    user_preferences_show_title_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowTitleToExternalUsers', verbose_name='ShowTitleToExternalUsers')
    user_preferences_show_manager_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowManagerToExternalUsers', verbose_name='ShowManagerToExternalUsers')
    user_preferences_show_email_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowEmailToExternalUsers', verbose_name='ShowEmailToExternalUsers')
    user_preferences_show_work_phone_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowWorkPhoneToExternalUsers', verbose_name='ShowWorkPhoneToExternalUsers')
    user_preferences_show_mobile_phone_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowMobilePhoneToExternalUsers', verbose_name='ShowMobilePhoneToExternalUsers')
    user_preferences_show_fax_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowFaxToExternalUsers', verbose_name='ShowFaxToExternalUsers')
    user_preferences_show_street_address_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowStreetAddressToExternalUsers', verbose_name='ShowStreetAddressToExternalUsers')
    user_preferences_show_city_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowCityToExternalUsers', verbose_name='ShowCityToExternalUsers')
    user_preferences_show_state_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowStateToExternalUsers', verbose_name='ShowStateToExternalUsers')
    user_preferences_show_postal_code_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowPostalCodeToExternalUsers', verbose_name='ShowPostalCodeToExternalUsers')
    user_preferences_show_country_to_external_users = models.BooleanField(
        db_column='UserPreferencesShowCountryToExternalUsers', verbose_name='ShowCountryToExternalUsers')
    user_preferences_show_profile_pic_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowProfilePicToGuestUsers', verbose_name='ShowProfilePicToGuestUsers')
    user_preferences_show_title_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowTitleToGuestUsers', verbose_name='ShowTitleToGuestUsers')
    user_preferences_show_city_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowCityToGuestUsers', verbose_name='ShowCityToGuestUsers')
    user_preferences_show_state_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowStateToGuestUsers', verbose_name='ShowStateToGuestUsers')
    user_preferences_show_postal_code_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowPostalCodeToGuestUsers', verbose_name='ShowPostalCodeToGuestUsers')
    user_preferences_show_country_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowCountryToGuestUsers', verbose_name='ShowCountryToGuestUsers')
    user_preferences_hide_s1_browser_ui = models.BooleanField(
        db_column='UserPreferencesHideS1BrowserUI', verbose_name='HideS1BrowserUI')
    user_preferences_disable_endorsement_email = models.BooleanField(
        db_column='UserPreferencesDisableEndorsementEmail', verbose_name='DisableEndorsementEmail')
    user_preferences_path_assistant_collapsed = models.BooleanField(
        db_column='UserPreferencesPathAssistantCollapsed', verbose_name='PathAssistantCollapsed')
    user_preferences_cache_diagnostics = models.BooleanField(
        db_column='UserPreferencesCacheDiagnostics', verbose_name='CacheDiagnostics')
    user_preferences_show_email_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowEmailToGuestUsers', verbose_name='ShowEmailToGuestUsers')
    user_preferences_show_manager_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowManagerToGuestUsers', verbose_name='ShowManagerToGuestUsers')
    user_preferences_show_work_phone_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowWorkPhoneToGuestUsers', verbose_name='ShowWorkPhoneToGuestUsers')
    user_preferences_show_mobile_phone_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowMobilePhoneToGuestUsers', verbose_name='ShowMobilePhoneToGuestUsers')
    user_preferences_show_fax_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowFaxToGuestUsers', verbose_name='ShowFaxToGuestUsers')
    user_preferences_show_street_address_to_guest_users = models.BooleanField(
        db_column='UserPreferencesShowStreetAddressToGuestUsers', verbose_name='ShowStreetAddressToGuestUsers')
    user_preferences_lightning_experience_preferred = models.BooleanField(
        db_column='UserPreferencesLightningExperiencePreferred', verbose_name='LightningExperiencePreferred')
    user_preferences_preview_lightning = models.BooleanField(
        db_column='UserPreferencesPreviewLightning', verbose_name='PreviewLightning')
    user_preferences_hide_end_user_onboarding_assistant_modal = models.BooleanField(
        db_column='UserPreferencesHideEndUserOnboardingAssistantModal', verbose_name='HideEndUserOnboardingAssistantModal')
    user_preferences_hide_lightning_migration_modal = models.BooleanField(
        db_column='UserPreferencesHideLightningMigrationModal', verbose_name='HideLightningMigrationModal')
    user_preferences_hide_sfx_welcome_mat = models.BooleanField(
        db_column='UserPreferencesHideSfxWelcomeMat', verbose_name='HideSfxWelcomeMat')
    user_preferences_hide_bigger_photo_callout = models.BooleanField(
        db_column='UserPreferencesHideBiggerPhotoCallout', verbose_name='HideBiggerPhotoCallout')
    user_preferences_global_nav_bar_wtshown = models.BooleanField(
        db_column='UserPreferencesGlobalNavBarWTShown', verbose_name='GlobalNavBarWTShown')
    user_preferences_global_nav_grid_menu_wtshown = models.BooleanField(
        db_column='UserPreferencesGlobalNavGridMenuWTShown', verbose_name='GlobalNavGridMenuWTShown')
    user_preferences_create_lexapps_wtshown = models.BooleanField(
        db_column='UserPreferencesCreateLEXAppsWTShown', verbose_name='CreateLEXAppsWTShown')
    user_preferences_favorites_wtshown = models.BooleanField(
        db_column='UserPreferencesFavoritesWTShown', verbose_name='FavoritesWTShown')
    user_preferences_record_home_section_collapse_wtshown = models.BooleanField(
        db_column='UserPreferencesRecordHomeSectionCollapseWTShown', verbose_name='RecordHomeSectionCollapseWTShown')
    user_preferences_record_home_reserved_wtshown = models.BooleanField(
        db_column='UserPreferencesRecordHomeReservedWTShown', verbose_name='RecordHomeReservedWTShown')
    user_preferences_favorites_show_top_favorites = models.BooleanField(
        db_column='UserPreferencesFavoritesShowTopFavorites', verbose_name='FavoritesShowTopFavorites')
    user_preferences_exclude_mail_app_attachments = models.BooleanField(
        db_column='UserPreferencesExcludeMailAppAttachments', verbose_name='ExcludeMailAppAttachments')
    user_preferences_suppress_task_sfxreminders = models.BooleanField(
        db_column='UserPreferencesSuppressTaskSFXReminders', verbose_name='SuppressTaskSFXReminders')
    user_preferences_suppress_event_sfxreminders = models.BooleanField(
        db_column='UserPreferencesSuppressEventSFXReminders', verbose_name='SuppressEventSFXReminders')
    user_preferences_preview_custom_theme = models.BooleanField(
        db_column='UserPreferencesPreviewCustomTheme', verbose_name='PreviewCustomTheme')
    user_preferences_has_celebration_badge = models.BooleanField(
        db_column='UserPreferencesHasCelebrationBadge', verbose_name='HasCelebrationBadge')
    user_preferences_user_debug_mode_pref = models.BooleanField(
        db_column='UserPreferencesUserDebugModePref', verbose_name='UserDebugModePref')
    user_preferences_srhoverride_activities = models.BooleanField(
        db_column='UserPreferencesSRHOverrideActivities', verbose_name='SRHOverrideActivities')
    user_preferences_new_lightning_report_run_page_enabled = models.BooleanField(
        db_column='UserPreferencesNewLightningReportRunPageEnabled', verbose_name='NewLightningReportRunPageEnabled')
    user_preferences_reverse_open_activities_view = models.BooleanField(
        db_column='UserPreferencesReverseOpenActivitiesView', verbose_name='ReverseOpenActivitiesView')
    user_preferences_show_territory_time_zone_shifts = models.BooleanField(
        db_column='UserPreferencesShowTerritoryTimeZoneShifts', verbose_name='ShowTerritoryTimeZoneShifts')
    user_preferences_native_email_client = models.BooleanField(
        db_column='UserPreferencesNativeEmailClient', verbose_name='NativeEmailClient')
    contact_id = models.CharField(db_column='ContactId', max_length=18, verbose_name='Contact ID',
                                  blank=True, null=True)  # References to missing tables: ['-Contact']
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='AccountId',
                                verbose_name='Account ID', sf_read_only=models.READ_ONLY, blank=True, null=True)
    call_center_id = models.CharField(db_column='CallCenterId', max_length=18, verbose_name='Call Center ID',
                                      blank=True, null=True)  # References to missing tables: ['-CallCenter']
    extension = models.CharField(
        db_column='Extension', max_length=40, blank=True, null=True)
    federation_identifier = models.CharField(
        db_column='FederationIdentifier', max_length=512, verbose_name='SAML Federation ID', blank=True, null=True)
    about_me = models.TextField(db_column='AboutMe', blank=True, null=True)
    full_photo_url = models.URLField(
        db_column='FullPhotoUrl', verbose_name='Url for full-sized Photo', sf_read_only=models.READ_ONLY, blank=True, null=True)
    small_photo_url = models.URLField(
        db_column='SmallPhotoUrl', verbose_name='Photo', sf_read_only=models.READ_ONLY, blank=True, null=True)
    is_ext_indicator_visible = models.BooleanField(
        db_column='IsExtIndicatorVisible', verbose_name='Show external indicator', sf_read_only=models.READ_ONLY, default=False)
    out_of_office_message = models.CharField(db_column='OutOfOfficeMessage', max_length=40,
                                             verbose_name='Out of office message', sf_read_only=models.READ_ONLY, blank=True, null=True)
    medium_photo_url = models.URLField(
        db_column='MediumPhotoUrl', verbose_name='Url for medium profile photo', sf_read_only=models.READ_ONLY, blank=True, null=True)
    digest_frequency = models.CharField(db_column='DigestFrequency', max_length=40, verbose_name='Chatter Email Highlights Frequency',
                                        default=models.DefaultedOnCreate('N'), choices=[('D', 'Daily'), ('W', 'Weekly'), ('N', 'Never')])
    default_group_notification_frequency = models.CharField(db_column='DefaultGroupNotificationFrequency', max_length=40, verbose_name='Default Notification Frequency when Joining Groups', default=models.DefaultedOnCreate(
        'N'), choices=[('P', 'Email on Each Post'), ('D', 'Daily Digests'), ('W', 'Weekly Digests'), ('N', 'Never')])
    jigsaw_import_limit_override = models.IntegerField(
        db_column='JigsawImportLimitOverride', verbose_name='Data.com Monthly Addition Limit', blank=True, null=True)
    last_viewed_date = models.DateTimeField(
        db_column='LastViewedDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_referenced_date = models.DateTimeField(
        db_column='LastReferencedDate', sf_read_only=models.READ_ONLY, blank=True, null=True)
    banner_photo_url = models.URLField(
        db_column='BannerPhotoUrl', verbose_name='Url for banner photo', sf_read_only=models.READ_ONLY, blank=True, null=True)
    small_banner_photo_url = models.URLField(
        db_column='SmallBannerPhotoUrl', verbose_name='Url for IOS banner photo', sf_read_only=models.READ_ONLY, blank=True, null=True)
    medium_banner_photo_url = models.URLField(
        db_column='MediumBannerPhotoUrl', verbose_name='Url for Android banner photo', sf_read_only=models.READ_ONLY, blank=True, null=True)
    is_profile_photo_active = models.BooleanField(
        db_column='IsProfilePhotoActive', verbose_name='Has Profile Photo', sf_read_only=models.READ_ONLY, default=False)
    individual_id = models.CharField(db_column='IndividualId', max_length=18, verbose_name='Individual ID',
                                     blank=True, null=True)  # References to missing tables: ['-Individual']

    class Meta(models.Model.Meta):
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # keyPrefix = '005'
