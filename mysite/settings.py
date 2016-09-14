"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'czh-8)nef97o9l$^1pdy=%n*%h8y*$ywq#t81$2a9eil5*t1jf'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False


ALLOWED_HOSTS = ['.XN--GENFERBRSE-KCB.COM']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'captcha',
    'responsive',
    'webmaster_verification',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'responsive.middleware.ResponsiveMiddleware'

)

ROOT_URLCONF = 'mysite.urls'
RECAPTCHA_PUBLIC_KEY = '6LcKhCkTAAAAAEUsKni7RYEbVoxfcoVkCFdm07AJ'
RECAPTCHA_PRIVATE_KEY = '6LcKhCkTAAAAAC9MwWDA6v_iikboF2Xc2bXD9kpr'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'responsive.context_processors.device'
            ],
        },
    },
]


WEBMASTER_VERIFICATION = {
    'google': 'googleacb34a5caa91b5c1',
}

RESPONSIVE_MEDIA_QUERIES = {

    # /* ----------- iPhone 4 and 4S ----------- */
    # /* vertical */
    'iphone4_v': {
        'verbose_name': _('iPhone 4'),
        'max_width': 320,  # mobile first queries
        'max_height': 480,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'iphone4_h': {
        'verbose_name': _('iPhone 4'),
        'max_height': 320,  # mobile first queries
        'max_width': 480,
        'pixel_ratio': 2
    },

    # /* ----------- iPhone 5 and 5S and 5SE----------- */
    # /* vertical */
    'iphone5_v': {
        'verbose_name': _('iPhone 5'),
        'max_width': 320,  # mobile first queries
        'max_height': 568,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'iphone5_h': {
        'verbose_name': _('iPhone 5'),
        'max_height': 568,  # mobile first queries
        'max_width': 320,
        'pixel_ratio': 2
    },

    # /* ----------- iPhone 6  ----------- */
    # /* vertical */
    'iphone6_v': {
        'verbose_name': _('iPhone 6'),
        'max_width': 375,  # mobile first queries
        'max_height': 667,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'iphone6_h': {
        'verbose_name': _('iPhone 6'),
        'max_height': 667,  # mobile first queries
        'min_height': 375,
        'min_width': 375,
        'max_width': 667,
        'pixel_ratio': 2
    },

    # /* ----------- iPhone 6 Plus ----------- */
    # /* vertical */
    'iphone6p_v': {
        'verbose_name': _('iPhone 6 Plus'),
        'max_width': 414,  # mobile first queries
        'max_height': 736,
        'pixel_ratio': 3
    },
    # /* horizontal */
    'iphone6p_h': {
        'verbose_name': _('iPhone 6 Plus'),
        'max_height': 736,  # mobile first queries
        'max_width': 414,
        'pixel_ratio': 3
    },

    # /* ----------- Galaxy S3 ----------- */
    # /* vertical */
    'galaxys3_v': {
        'verbose_name': _('Galaxy S3'),
        'max_width': 360,  # mobile first queries
        'max_height': 640,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'galaxys3_h': {
        'verbose_name': _('Galaxy S3'),
        'max_height': 640,  # mobile first queries
        'max_width': 360,
        'pixel_ratio': 2
    },

    # /* ----------- Galaxy S4 ----------- */
    # /* vertical */
    'galaxys4_v': {
        'verbose_name': _('Galaxy S4'),
        'max_width': 320,  # mobile first queries
        'max_height': 640,
        'pixel_ratio': 3
    },
    # /* horizontal */
    'galaxys4_h': {
        'verbose_name': _('Galaxy S4'),
        'max_height': 640,  # mobile first queries
        'max_width': 320,
        'pixel_ratio': 3
    },

    # /* ----------- Galaxy S5 ----------- */
    # /* vertical */
    'galaxys5_v': {
        'verbose_name': _('Galaxy S5'),
        'max_width': 360,  # mobile first queries
        'max_height': 640,
        'pixel_ratio': 3
    },
    # /* horizontal */
    'galaxys5_h': {
        'verbose_name': _('Galaxy S5'),
        'max_height': 360,  # mobile first queries
        'max_width': 640,
        'pixel_ratio': 3
    },

    # /* ----------- Nexus 5X ----------- */
    # /* vertical */
    'nexus5x_v': {
        'verbose_name': _('Nexus 5X'),
        'max_width': 412,  # mobile first queries
        'max_height': 732,
        'pixel_ratio': 2.6
    },
    # /* horizontal */
    'nexus5x_h': {
        'verbose_name': _('Nexus 5X'),
        'max_height': 732,  # mobile first queries
        'max_width': 412,
        'pixel_ratio': 2.6
    },

    # /* ----------- Galaxy Note 2 ----------- */
    # /* vertical */
    'galaxyn2_v': {
        'verbose_name': _('Galaxy Note 2'),
        'max_width': 360,  # mobile first queries
        'max_height': 640,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'galaxyn2_h': {
        'verbose_name': _('Galaxy Note 2'),
        'max_height': 640,  # mobile first queries
        'max_width': 360,
        'pixel_ratio': 2
    },

    # /* ----------- Nexus 6 ----------- */
    # /* vertical */
    'nexus6_v': {
        'verbose_name': _('Nexus 6'),
        'max_width': 412,  # mobile first queries
        'max_height': 732,
        'pixel_ratio': 3
    },
    # /* horizontal */
    'nexus6_h': {
        'verbose_name': _('Nexus 6'),
        'max_height': 732,  # mobile first queries
        'max_width': 412,
        'pixel_ratio': 3
    },

    # /* ----------- Nexus 7 ----------- */
    # /* vertical */
    'nexus7_v': {
        'verbose_name': _('Nexus 7'),
        'max_width': 690,  # mobile first queries
        'max_height': 960,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'nexus7_h': {
        'verbose_name': _('Nexus 7'),
        'max_height': 960,  # mobile first queries
        'max_width': 690,
        'pixel_ratio': 2
    },

    # /* ----------- Nokia Lumia 520 ----------- */
    # /* vertical */
    'lumia520_v': {
        'verbose_name': _('Nokia Lumia 520'),
        'max_width': 320,  # mobile first queries
        'max_height': 533,
        'pixel_ratio': 1.4
    },
    # /* horizontal */
    'lumia520_h': {
        'verbose_name': _('Nokia Lumia 520'),
        'max_height': 533,  # mobile first queries
        'max_width': 320,
        'pixel_ratio': 1.4
    },

    # /* ----------- Nokia N9 ----------- */
    # /* vertical */
    'nokian9_v': {
        'verbose_name': _('NNokia N9'),
        'max_width': 360,  # mobile first queries
        'max_height': 640,
        'pixel_ratio': 1
    },
    # /* horizontal */
    'nokian9_h': {
        'verbose_name': _('Nokia N9'),
        'max_height': 640,  # mobile first queries
        'max_width': 360,
        'pixel_ratio': 1
    },

    # /* ----------- Ipad mini ----------- */
    # /* vertical */
    'ipadm_v': {
        'verbose_name': _('Ipad mini'),
        'max_width': 768,  # mobile first queries
        'max_height': 1024,
        'pixel_ratio': 1
    },
    # /* horizontal */
    'ipadm_h': {
        'verbose_name': _('Ipad mini'),
        'max_height': 1024,  # mobile first queries
        'max_width': 768,
        'pixel_ratio': 1
    },

    # /* ----------- Ipad ----------- */
    # /* vertical */
    'ipad_v': {
        'verbose_name': _('Ipad'),
        'max_width': 768,  # mobile first queries
        'max_height': 1024,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'ipad_h': {
        'verbose_name': _('Ipad'),
        'max_height': 1024,  # mobile first queries
        'max_width': 768,
        'pixel_ratio': 2
    },

    # /* ----------- Galaxy Tab 10.1 ----------- */
    # /* vertical */
    'galaxytab_v': {
        'verbose_name': _('Galaxy Tab'),
        'max_width': 800,  # mobile first queries
        'max_height': 1280,
        'pixel_ratio': 1
    },
    # /* horizontal */
    'galaxytab_h': {
        'verbose_name': _('Galaxy Tab'),
        'max_height': 1280,  # mobile first queries
        'max_width': 800,
        'pixel_ratio': 1
    },

    # /* ----------- Kindle Fire HD 7 ----------- */
    # /* vertical */
    'kindle7_v': {
        'verbose_name': _('Kindle HD 7'),
        'max_width': 800,  # mobile first queries
        'max_height': 1280,
        'pixel_ratio': 1.5
    },
    # /* horizontal */
    'kindle7_h': {
        'verbose_name': _('Kindle HD 7'),
        'max_height': 1280,  # mobile first queries
        'max_width': 800,
        'pixel_ratio': 1.5
    },
    # /* ----------- Kindle HDX ----------- */
    # /* vertical */
    'kindlehdx_v': {
        'verbose_name': _('Kindle HDX'),
        'max_width': 1600,  # mobile first queries
        'max_height': 2560,
        'pixel_ratio': 2
    },
    # /* horizontal */
    'kindlehdx_h': {
        'verbose_name': _('Kindle HDX'),
        'max_height': 2560,  # mobile first queries
        'max_width': 1600,
        'pixel_ratio': 2
    },

    # /* ----------- Laptop small ----------- */
    # /* vertical */
    'laptops': {
        'verbose_name': _('NLaptop small'),
        'max_width': 1280,  # mobile first queries
        'max_height': 800,
    },


    # /* ----------- Laptop Medium ----------- */
    # /* vertical */
    'laptopm': {
        'verbose_name': _('Laptop medium'),
        'max_width': 1366,  # mobile first queries
        'max_height': 768,
    },

    # /* ----------- Laptop Large ----------- */
    # /* vertical */
    'laptopl': {
        'verbose_name': _('Laptop Large'),
        'max_width': 1800,  # mobile first queries
        'max_height': 1000,
        'min_width': 1367,
        'min_heiht': 769
    },

    # /* ----------- Retina  ----------- */
    # /* vertical */
    'retina': {
        'pixel_ratio': 2,
        'verbouse_name': 'Retina'
    },


}

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
