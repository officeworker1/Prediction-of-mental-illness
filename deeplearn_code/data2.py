import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
from second_deeplearn.data import imp_data

sns.set_style('whitegrid')
sns.set_palette('Set2')
mpl.rcParams['font.size'] = 16
import matplotlib.gridspec as gridspec
# Most respondents are tech and also most of them are in US.
# Most techs are in medium and large companies
# For future analysis, we will exclude all people non-tech - as this analysis focuses on mental health in tech

# Most respondents are male

# Most respondents are tech and also most of them are in US.
# Most techs are in medium and large companies
# For future analysis, we will exclude all people non-tech - as this analysis focuses on mental health in tech

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
plt.figure(figsize = (16,4))
fig.set_figheight(5)
fig.set_figwidth(20)
plt.subplots_adjust(wspace = 0)
# plt.suptitle('Main Title')

# No of respondents by Country
sns.countplot(x = imp_data['country_live'], hue = imp_data['tech_flag'], ax=ax1)
ax1.set_title('No. of Respondents by Country and tech_flag', fontsize = 20)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=15, ha="right")
ax1.set_xlabel('Country', fontsize = 18)
ax1.set_ylabel('Count', fontsize = 18)
ax1.legend(['Not in Tech', 'In Tech'])

# No of respondents by Company Size
sns.countplot(x = imp_data['comp_no_empl'], hue = imp_data['tech_flag'], ax=ax2,
              order = ['1-5', '6-25', '26-100', '100-500', '500-1000', '>1000'])
ax2.set_title('No. of Respondents by Company Size and tech_flag', fontsize = 20)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=15, ha="right")
ax2.set_xlabel('Company Size', fontsize = 18)
ax2.set_ylabel('Count', fontsize = 18)
ax2.legend(['Not in Tech', 'In Tech']);
# Most respondents are male

plt.figure(figsize = (16,5))
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(20)
plt.subplots_adjust(wspace = 0)
fig.suptitle('Proportions of genders in tech', fontsize = 25, y=1.08)

# Pie Chart
all_techs = imp_data[imp_data['tech_flag'] == 1]['sex'].count()
males = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['sex'] == 1.0)]['sex'].count()
females = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['sex'] == 2.0)]['sex'].count()
other = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['sex'] == 3.0)]['sex'].count()

labels = 'Male', 'Female', 'Other'
sizes = [males/all_techs, females/all_techs, other/all_techs]
colors = ['#73C6B6', '#F0B27A', '#7FB3D5']
explode = (0.03, 0, 0)  # explode 1st slice

ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax2.axis('equal')
ax2.set_title('Overall gender prop%', pad = 20, fontsize = 20)

# Barchart
sns.countplot(x = imp_data[imp_data['tech_flag'] == 1]['country_live'], hue = imp_data['sex'], ax = ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=15, ha="right")
ax1.set_title('Gender by Countries', pad = 20, fontsize = 20)
ax1.set_xlabel('Country', fontsize = 18)
ax1.set_ylabel('Count', fontsize = 18)
ax1.legend(['Male', 'Female', 'Other']);
imp_data[imp_data['tech_flag'] == 1]['age'].describe()
# ----------- NOW -----------

plt.figure(figsize = (16,5))
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(20)
plt.subplots_adjust(wspace = 0)
fig.suptitle('Mental Health Disorder in Tech (in the present)', fontsize = 25, y=1.08)

# Pie Chart (Now)
all_techs_now = imp_data[imp_data['tech_flag'] == 1]['mh_disorder_current'].count()
no_now = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_current'] == 'No')]['mh_disorder_current'].count()
yes_now = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_current'] == 'Yes')]['mh_disorder_current'].count()
maybe_now = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_current'] == 'Maybe')]['mh_disorder_current'].count()

labels = 'No', 'Yes', 'Maybe'
sizes = [no_now/all_techs_now, yes_now/all_techs_now, maybe_now/all_techs_now]
colors = ['#73C6B6', '#F0B27A', '#7FB3D5']
explode = (0, 0.03, 0)  # explode 1st slice

ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax2.axis('equal')
ax2.set_title('Overall MH prop% (NOW)', pad = 20, fontsize = 20)

# Barchart (now)
sns.countplot(x = imp_data[imp_data['tech_flag'] == 1]['country_live'], hue = imp_data['mh_disorder_current'], ax = ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=15, ha="right")
ax1.set_title('MH by Countries (NOW)', pad = 20, fontsize = 20)
ax1.set_xlabel('Country', fontsize = 18)
ax1.set_ylabel('Count', fontsize = 18)
ax1.legend();
# ----------- PAST -----------

_ = plt.figure(figsize = (16,5))
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(20)
plt.subplots_adjust(wspace = 0)
fig.suptitle('Mental Health Disorder in Tech (in the past)', fontsize = 25, y=1.08)

# Pie Chart (Past)
all_techs_past = imp_data[imp_data['tech_flag'] == 1]['mh_disorder_current'].count()
no_past = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_past'] == 'No')]['mh_disorder_past'].count()
yes_past = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_past'] == 'Yes')]['mh_disorder_past'].count()
maybe_past = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_past'] == 'Maybe')]['mh_disorder_past'].count()

labels = 'No', 'Yes', 'Maybe'
sizes = [no_past/all_techs_past, yes_past/all_techs_past, maybe_past/all_techs_past]
colors = ['#73C6B6', '#F0B27A', '#7FB3D5']
explode = (0, 0.03, 0)  # explode 1st slice

ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax2.axis('equal')
ax2.set_title('Overall MH prop% (PAST)', pad = 20, fontsize = 20)

# Barchart (Past)
sns.countplot(x = imp_data[imp_data['tech_flag'] == 1]['country_live'], hue = imp_data['mh_disorder_past'], ax = ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=15, ha="right")
ax1.set_title('MH by Countries (PAST)', pad = 20, fontsize = 20)
ax1.set_xlabel('Country', fontsize = 18)
ax1.set_ylabel('Count', fontsize = 18)
ax1.legend();
mpl.rcParams['font.size'] = 13

fig, ax = plt.subplots(figsize = (16, 12), ncols=2, nrows=3)
plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top = 0.9, wspace=0, hspace = 0.3)
plt.suptitle('Are the Companies taking seriously mental health?', fontsize = 25, y = 1)

# Does your employer provide mental health benefits as part of healthcare coverage?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_coverage_flag'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_coverage_flag'] == 'No')]['mh_coverage_flag'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_coverage_flag'] == 'Yes')]['mh_coverage_flag'].count()
not_know_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_coverage_flag'] == "I don't know")]['mh_coverage_flag'].count()
not_elig_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_coverage_flag'] == 'Not eligible for coverage / N/A')]['mh_coverage_flag'].count()

labels = 'No', 'Yes', 'Not Know', 'Not Elig.'
sizes = [no_/all_, yes_/all_, not_know_/all_, not_elig_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A', '#C39BD3']
explode = (0, 0.03, 0, 0)  # explode 1st slice

ax[0][0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[0][0].axis('equal')
ax[0][0].set_title('MH Coverage Provided', pad = 14, fontsize = 18)

# Does your employer offer resources to learn more about mental health concerns and options for seeking help?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_resources_provided'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_resources_provided'] == 'No')]['mh_resources_provided'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_resources_provided'] == 'Yes')]['mh_resources_provided'].count()
not_know_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_resources_provided'] == "I don't know")]['mh_resources_provided'].count()

labels = 'No', 'Yes', 'Not Know'
sizes = [no_/all_, yes_/all_, not_know_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A']
explode = (0.03, 0, 0)  # explode 1st slice

ax[0][1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[0][1].axis('equal')
ax[0][1].set_title('MH Resources Provided', pad = 14, fontsize = 18)

# Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_anonimity_flag'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_anonimity_flag'] == 'No')]['mh_anonimity_flag'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_anonimity_flag'] == 'Yes')]['mh_anonimity_flag'].count()
not_know_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_anonimity_flag'] == "I don't know")]['mh_anonimity_flag'].count()

labels = 'No', 'Yes', 'Not Know'
sizes = [no_/all_, yes_/all_, not_know_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A']
explode = (0, 0, 0.03)  # explode 1st slice

ax[1][0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[1][0].axis('equal')
ax[1][0].set_title('MH Anonimity Provided', pad = 14, fontsize = 18)

# If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_medical_leave'].count()
veasy_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_medical_leave'] == 'Very easy')]['mh_medical_leave'].count()
seasy_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_medical_leave'] == 'Somewhat easy')]['mh_medical_leave'].count()
middle_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_medical_leave'] == "Neither easy nor difficult")]['mh_medical_leave'].count()
vdiff_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_medical_leave'] == "Very difficult")]['mh_medical_leave'].count()
sdiff_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_medical_leave'] == "Somewhat difficult")]['mh_medical_leave'].count()
not_know_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_medical_leave'] == "I don't know")]['mh_medical_leave'].count()

labels = 'V Easy', 'S Easy', 'Middle', 'V Difficult', 'S Difficult', 'Not Know'
sizes = [veasy_/all_, seasy_/all_, middle_/all_, vdiff_/all_, sdiff_/all_, not_know_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A', '#C39BD3', '#ABEBC6', '#F4D03F']
explode = (0, 0.03, 0, 0, 0, 0)  # explode 1st slice

ax[1][1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[1][1].axis('equal')
ax[1][1].set_title('MH Medical Leave Request', pad = 14, fontsize = 18)

# Do you feel that your employer takes mental health as seriously as physical health?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_eq_ph_employer'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_eq_ph_employer'] == 'No')]['mh_eq_ph_employer'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_eq_ph_employer'] == 'Yes')]['mh_eq_ph_employer'].count()
not_know_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_eq_ph_employer'] == "I don't know")]['mh_eq_ph_employer'].count()

labels = 'No', 'Yes', 'Not Know'
sizes = [no_/all_, yes_/all_, not_know_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A']
explode = (0, 0, 0.03)  # explode 1st slice

ax[2][0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[2][0].axis('equal')
ax[2][0].set_title('Mental & Physical Health Equal Importance', pad = 14, fontsize = 18)

# Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_conseq_coworkers'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_conseq_coworkers'] == 'No')]['mh_conseq_coworkers'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_conseq_coworkers'] == 'Yes')]['mh_conseq_coworkers'].count()

labels = 'No', 'Yes'
sizes = [no_/all_, yes_/all_]
colors = ['#7FB3D5', '#73C6B6']
explode = (0.08, 0)  # explode 1st slice

ax[2][1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[2][1].axis('equal')
ax[2][1].set_title('Neg. Conseq for Coworkers with MH Disorders', pad = 14, fontsize = 18);
fig, ax = plt.subplots(figsize = (16, 8), ncols=2, nrows=2)
plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top = 0.9, wspace=0, hspace = 0.3)
plt.suptitle('Discussing Mental Health at Work', fontsize = 25, y = 1.04)

# Do you think that discussing a mental health disorder with your employer would have negative consequences?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_discussion_neg_impact'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_neg_impact'] == 'No')]['mh_discussion_neg_impact'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_neg_impact'] == 'Yes')]['mh_discussion_neg_impact'].count()
maybe_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_neg_impact'] == 'Maybe')]['mh_discussion_neg_impact'].count()

labels = 'No', 'Yes', 'Not Know'
sizes = [no_/all_, yes_/all_, maybe_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A']
explode = (0, 0, 0.03)  # explode 1st slice

ax[0][0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[0][0].axis('equal')
ax[0][0].set_title('Neg Consequences after Discussing MH with Employer', pad = 14, fontsize = 14)

# Would you feel comfortable discussing a mental health disorder with your coworkers?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_discussion_cowork'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_cowork'] == 'No')]['mh_discussion_cowork'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_cowork'] == 'Yes')]['mh_discussion_cowork'].count()
maybe_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_cowork'] == 'Maybe')]['mh_discussion_cowork'].count()

labels = 'No', 'Yes', 'Not Know'
sizes = [no_/all_, yes_/all_, maybe_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A']
explode = (0, 0, 0.03)  # explode 1st slice

ax[0][1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[0][1].axis('equal')
ax[0][1].set_title('Are you relaxed of talking MHD with coworkers?', pad = 14, fontsize = 14)

# Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_neg_view_cowork'].count()
no_t = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_neg_view_cowork'] == "No, I don't think they would")]['mh_neg_view_cowork'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_neg_view_cowork'] == "No, they do not")]['mh_neg_view_cowork'].count()
maybe_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_neg_view_cowork'] == 'Maybe')]['mh_neg_view_cowork'].count()
yes_t = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_neg_view_cowork'] == 'Yes, I think they would')]['mh_neg_view_cowork'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_neg_view_cowork'] == 'Yes, they do')]['mh_neg_view_cowork'].count()

labels = 'I think no', 'They do not', 'Maybe', 'I think yes', 'They do'
sizes = [no_t/all_, no_/all_, maybe_/all_, yes_t/all_, yes_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A', '#C39BD3', '#ABEBC6']
explode = (0, 0, 0.03, 0, 0)  # explode 1st slice

ax[1][0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[1][0].axis('equal')
ax[1][0].set_title('You think coworkers will view you badly after confessing to a MHD?', pad = 14, fontsize = 14)

# Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_discussion_supervis'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_supervis'] == 'No')]['mh_discussion_supervis'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_supervis'] == 'Yes')]['mh_discussion_supervis'].count()
maybe_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_discussion_supervis'] == 'Maybe')]['mh_discussion_supervis'].count()

labels = 'No', 'Yes', 'Not Know'
sizes = [no_/all_, yes_/all_, maybe_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A']
explode = (0, 0.03, 0)  # explode 1st slice

ax[1][1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax[1][1].axis('equal')
ax[1][1].set_title('Are you relaxed of talking MHD with supervisors?', pad = 14, fontsize = 14);
fig, (ax1, ax2) = plt.subplots(figsize = (16, 4), ncols=2, nrows=1)
plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top = 0.9, wspace=0, hspace = 0.3)
plt.suptitle('Is MH having bad consequences on career?', fontsize = 23, y = 1.1)

# Do you feel that being identified as a person with a mental health issue would hurt your career?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_hurt_on_career'].count()
no_t = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_hurt_on_career'] == "No, I don't think it would")]['mh_hurt_on_career'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_hurt_on_career'] == "No, it has not")]['mh_hurt_on_career'].count()
maybe_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_hurt_on_career'] == 'Maybe')]['mh_hurt_on_career'].count()
yes_t = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_hurt_on_career'] == 'Yes, I think it would')]['mh_hurt_on_career'].count()
yes_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_hurt_on_career'] == 'Yes, it has')]['mh_hurt_on_career'].count()

labels = 'I think no', 'It has not', 'Maybe', 'I think yes', 'Yes it has'
sizes = [no_t/all_, no_/all_, maybe_/all_, yes_t/all_, yes_/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A', '#C39BD3', '#ABEBC6']
explode = (0, 0, 0.03, 0, 0)  # explode 1st slice

ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax1.axis('equal')
ax1.set_title('You think being a person with MHD can hurt your career?', pad = 14, fontsize = 14)

# Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_bad_response_workplace'].count()
no_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_bad_response_workplace'] == "No")]['mh_bad_response_workplace'].count()
maybe_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_bad_response_workplace'] == 'Maybe/Not sure')]['mh_bad_response_workplace'].count()
yes_e = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_bad_response_workplace'] == 'Yes, I experienced')]['mh_bad_response_workplace'].count()
yes_o = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_bad_response_workplace'] == 'Yes, I observed')]['mh_bad_response_workplace'].count()

labels = 'No', 'Maybe/Not sure', 'Yes, I experienced', 'Yes, I observed'
sizes = [no_/all_, maybe_/all_, yes_e/all_, yes_o/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A', '#C39BD3']
explode = (0.03, 0, 0, 0)  # explode 1st slice

ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
ax2.axis('equal')
ax2.set_title('Have you observed/experienced badly response to a MHD?', pad = 14, fontsize = 14);
plt.figure(figsize = (16, 5))

# How willing would you be to share with friends and family that you have a mental illness?
all_ = imp_data[imp_data['tech_flag'] == 1]['mh_sharing_friends/fam_flag'].count()
na_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_sharing_friends/fam_flag'] == "Not applicable to me (I do not have a mental illness)")]['mh_sharing_friends/fam_flag'].count()
not_open_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_sharing_friends/fam_flag'] == 'Not open at all')]['mh_sharing_friends/fam_flag'].count()
somewhat_no = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_sharing_friends/fam_flag'] == 'Somewhat not open')]['mh_sharing_friends/fam_flag'].count()
neutral_ = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_sharing_friends/fam_flag'] == 'Neutral')]['mh_sharing_friends/fam_flag'].count()
somewhat_o = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_sharing_friends/fam_flag'] == 'Somewhat open')]['mh_sharing_friends/fam_flag'].count()
very_o = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_sharing_friends/fam_flag'] == 'Very open')]['mh_sharing_friends/fam_flag'].count()

labels = 'NA to me', 'Not open at all', 'Somewhat not open', 'Neutral', 'Somewhat open', 'Very open'
sizes = [na_/all_, not_open_/all_, somewhat_no/all_, neutral_/all_, somewhat_o/all_, very_o/all_]
colors = ['#7FB3D5', '#73C6B6', '#F0B27A', '#C39BD3', '#ABEBC6', '#F4D03F']
explode = (0, 0, 0, 0, 0.03, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.title('How willing would you be to share with friends/family that you have a MHD?', pad = 14, fontsize = 20);
plt.show()
# Preparing the data

# Create the table
table0 = imp_data[(imp_data['country_work'] == 'USA') & (imp_data['tech_flag'] == 1)].groupby(by = ['work_us_teritory', 'mh_disorder_current'])['self_empl_flag'].count().reset_index()
table1 = table0.pivot(index = 'work_us_teritory', columns = 'mh_disorder_current', values = 'self_empl_flag').reset_index()

# Deal with all NaN (setting them to 0)
table1.fillna(0, inplace = True)

# Calculate a prop column
table1['prop'] = table1['Yes'] / (table1['Maybe'] + table1['No'] + table1['Yes']) * 100
table1.rename(columns = {'work_us_teritory' : 'State'}, inplace = True)

# Add State Codes
codes = pd.read_csv('../input/usa-information/states.csv')
table2 = pd.merge(left = table1, right=codes, how = 'inner', on = 'State') #we lost none of the data :)

# Final table
df = table2[['State', 'Abbreviation', 'prop']]

# Creating the map

import plotly.graph_objects as go

fig = go.Figure(data=go.Choropleth(
    locations=df['Abbreviation'], # Spatial coordinates
    z = df['prop'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "Percentage(%)",
    text = df['State'],
    marker_line_color='lightgray',
    marker_line_width=1
))

fig.update_layout(
    title_text = 'Percentage of people with MHD in every state (from total respondents)',
    geo_scope='usa', # limite map scope to USA
)
plt.show()