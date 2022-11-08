--
-- PostgreSQL database dump
--

-- Dumped from database version 14.0 (Debian 14.0-1.pgdg110+1)
-- Dumped by pg_dump version 14.0 (Debian 14.0-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: api_accessibleelement; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_accessibleelement (
    _id integer NOT NULL,
    _text text NOT NULL,
    _pictogram text NOT NULL
);


ALTER TABLE public.api_accessibleelement OWNER TO admin;

--
-- Name: api_accesibleelement__id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_accessibleelement ALTER COLUMN _id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_accesibleelement__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: api_classroom; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_classroom (
    _id integer NOT NULL,
    _class_code_id integer NOT NULL
);


ALTER TABLE public.api_classroom OWNER TO admin;

--
-- Name: api_classroom__id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_classroom ALTER COLUMN _id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_classroom__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: api_dish; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_dish (
    _id integer NOT NULL,
    _name_id integer NOT NULL,
    _type_id character varying(20) NOT NULL
);


ALTER TABLE public.api_dish OWNER TO admin;

--
-- Name: api_dish__id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_dish ALTER COLUMN _id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_dish__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: api_dishtype; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_dishtype (
    _id character varying(20) NOT NULL
);


ALTER TABLE public.api_dishtype OWNER TO admin;

--
-- Name: api_feedback; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_feedback (
    _id integer NOT NULL,
    _feedback_id integer NOT NULL
);


ALTER TABLE public.api_feedback OWNER TO admin;

--
-- Name: api_feedback__id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_feedback ALTER COLUMN _id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_feedback__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: api_kitchenorder; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_kitchenorder (
    id bigint NOT NULL,
    _id_id integer NOT NULL
);


ALTER TABLE public.api_kitchenorder OWNER TO admin;

--
-- Name: api_kitchenorder_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_kitchenorder ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_kitchenorder_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: api_kitchenorderdetail; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_kitchenorderdetail (
    _id integer NOT NULL,
    _quantity integer NOT NULL,
    _classroom_id integer NOT NULL,
    _dish_id integer NOT NULL,
    _kitchen_order_id bigint NOT NULL
);


ALTER TABLE public.api_kitchenorderdetail OWNER TO admin;

--
-- Name: api_kitchenorderdetail__id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_kitchenorderdetail ALTER COLUMN _id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_kitchenorderdetail__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: api_task; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.api_task (
    _id integer NOT NULL,
    _due_date date NOT NULL,
    _feedback_id integer,
    _name_id integer NOT NULL
);


ALTER TABLE public.api_task OWNER TO admin;

--
-- Name: api_task__id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.api_task ALTER COLUMN _id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.api_task__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Data for Name: api_accessibleelement; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_accessibleelement (_id, _text, _pictogram) FROM stdin;
4	Clase D	https://static.vecteezy.com/system/resources/previews/000/401/729/original/vector-capital-letter-a-vintage-typography-style.jpg
5	Clase E	https://static.vecteezy.com/system/resources/previews/000/401/729/original/vector-capital-letter-a-vintage-typography-style.jpg
3	Clase C	https://static.vecteezy.com/system/resources/previews/000/401/729/original/vector-capital-letter-a-vintage-typography-style.jpg
2	Clase B	https://static.vecteezy.com/system/resources/previews/000/401/729/original/vector-capital-letter-a-vintage-typography-style.jpg
1	Clase A	https://api.arasaac.org/api/pictograms/4610?resolution=500&download=false\n
6	Clase F	https://static.vecteezy.com/system/resources/previews/000/401/729/original/vector-capital-letter-a-vintage-typography-style.jpg
8	Petición Material	https://api.arasaac.org/api/pictograms/15838?resolution=500&download=false
7	La Comanda	https://api.arasaac.org/api/pictograms/4610?resolution=500&download=false
9	Con Carne	https://api.arasaac.org/api/pictograms/6961?resolution=500&download=false
10	Huevo	https://api.arasaac.org/api/pictograms/35917?resolution=500&download=false
11	Fruta	https://api.arasaac.org/api/pictograms/4653?resolution=500&download=false
\.


--
-- Data for Name: api_classroom; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_classroom (_id, _class_code_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
\.


--
-- Data for Name: api_dish; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_dish (_id, _name_id, _type_id) FROM stdin;
1	9	MENU
2	10	MENU
3	11	POSTRE
\.


--
-- Data for Name: api_dishtype; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_dishtype (_id) FROM stdin;
MENU
POSTRE
\.


--
-- Data for Name: api_feedback; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_feedback (_id, _feedback_id) FROM stdin;
\.


--
-- Data for Name: api_kitchenorder; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_kitchenorder (id, _id_id) FROM stdin;
1	1
\.


--
-- Data for Name: api_kitchenorderdetail; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_kitchenorderdetail (_id, _quantity, _classroom_id, _dish_id, _kitchen_order_id) FROM stdin;
\.


--
-- Data for Name: api_task; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.api_task (_id, _due_date, _feedback_id, _name_id) FROM stdin;
1	2022-03-22	\N	7
2	2022-11-22	\N	8
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add accesible element	7	add_accesibleelement
26	Can change accesible element	7	change_accesibleelement
27	Can delete accesible element	7	delete_accesibleelement
28	Can view accesible element	7	view_accesibleelement
29	Can add classroom	8	add_classroom
30	Can change classroom	8	change_classroom
31	Can delete classroom	8	delete_classroom
32	Can view classroom	8	view_classroom
33	Can add dish	9	add_dish
34	Can change dish	9	change_dish
35	Can delete dish	9	delete_dish
36	Can view dish	9	view_dish
37	Can add dish type	10	add_dishtype
38	Can change dish type	10	change_dishtype
39	Can delete dish type	10	delete_dishtype
40	Can view dish type	10	view_dishtype
41	Can add feedback	11	add_feedback
42	Can change feedback	11	change_feedback
43	Can delete feedback	11	delete_feedback
44	Can view feedback	11	view_feedback
45	Can add kitchen order	12	add_kitchenorder
46	Can change kitchen order	12	change_kitchenorder
47	Can delete kitchen order	12	delete_kitchenorder
48	Can view kitchen order	12	view_kitchenorder
49	Can add task	13	add_task
50	Can change task	13	change_task
51	Can delete task	13	delete_task
52	Can view task	13	view_task
53	Can add kitchen order detail	14	add_kitchenorderdetail
54	Can change kitchen order detail	14	change_kitchenorderdetail
55	Can delete kitchen order detail	14	delete_kitchenorderdetail
56	Can view kitchen order detail	14	view_kitchenorderdetail
57	Can add accessible element	7	add_accessibleelement
58	Can change accessible element	7	change_accessibleelement
59	Can delete accessible element	7	delete_accessibleelement
60	Can view accessible element	7	view_accessibleelement
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
8	api	classroom
9	api	dish
10	api	dishtype
11	api	feedback
12	api	kitchenorder
13	api	task
14	api	kitchenorderdetail
7	api	accessibleelement
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-11-02 22:56:41.621891+00
2	auth	0001_initial	2022-11-02 22:56:41.979848+00
3	admin	0001_initial	2022-11-02 22:56:42.150636+00
4	admin	0002_logentry_remove_auto_add	2022-11-02 22:56:42.185751+00
5	admin	0003_logentry_add_action_flag_choices	2022-11-02 22:56:42.22249+00
6	api	0001_initial	2022-11-02 22:56:42.687031+00
7	api	0002_rename__accesible_element_feedback__feedback	2022-11-02 22:56:42.81162+00
8	contenttypes	0002_remove_content_type_name	2022-11-02 22:56:42.846979+00
9	auth	0002_alter_permission_name_max_length	2022-11-02 22:56:42.857604+00
10	auth	0003_alter_user_email_max_length	2022-11-02 22:56:42.875642+00
11	auth	0004_alter_user_username_opts	2022-11-02 22:56:42.891269+00
12	auth	0005_alter_user_last_login_null	2022-11-02 22:56:42.905929+00
13	auth	0006_require_contenttypes_0002	2022-11-02 22:56:42.910753+00
14	auth	0007_alter_validators_add_error_messages	2022-11-02 22:56:42.927287+00
15	auth	0008_alter_user_username_max_length	2022-11-02 22:56:42.95836+00
16	auth	0009_alter_user_last_name_max_length	2022-11-02 22:56:42.970105+00
17	auth	0010_alter_group_name_max_length	2022-11-02 22:56:42.987723+00
18	auth	0011_update_proxy_permissions	2022-11-02 22:56:43.009126+00
19	auth	0012_alter_user_first_name_max_length	2022-11-02 22:56:43.02282+00
20	sessions	0001_initial	2022-11-02 22:56:43.080639+00
21	api	0003_rename_accesibleelement_accessibleelement	2022-11-04 18:23:11.969055+00
22	api	0004_alter_task__feedback	2022-11-07 17:40:07.646677+00
23	api	0005_alter_task__feedback	2022-11-07 17:56:29.944697+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Name: api_accesibleelement__id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_accesibleelement__id_seq', 11, true);


--
-- Name: api_classroom__id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_classroom__id_seq', 6, true);


--
-- Name: api_dish__id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_dish__id_seq', 3, true);


--
-- Name: api_feedback__id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_feedback__id_seq', 1, false);


--
-- Name: api_kitchenorder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_kitchenorder_id_seq', 1, true);


--
-- Name: api_kitchenorderdetail__id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_kitchenorderdetail__id_seq', 1, false);


--
-- Name: api_task__id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.api_task__id_seq', 2, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 23, true);


--
-- Name: api_accessibleelement api_accesibleelement_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_accessibleelement
    ADD CONSTRAINT api_accesibleelement_pkey PRIMARY KEY (_id);


--
-- Name: api_classroom api_classroom_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_classroom
    ADD CONSTRAINT api_classroom_pkey PRIMARY KEY (_id);


--
-- Name: api_dish api_dish_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_dish
    ADD CONSTRAINT api_dish_pkey PRIMARY KEY (_id);


--
-- Name: api_dishtype api_dishtype_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_dishtype
    ADD CONSTRAINT api_dishtype_pkey PRIMARY KEY (_id);


--
-- Name: api_feedback api_feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_feedback
    ADD CONSTRAINT api_feedback_pkey PRIMARY KEY (_id);


--
-- Name: api_kitchenorder api_kitchenorder_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_kitchenorder
    ADD CONSTRAINT api_kitchenorder_pkey PRIMARY KEY (id);


--
-- Name: api_kitchenorderdetail api_kitchenorderdetail_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_kitchenorderdetail
    ADD CONSTRAINT api_kitchenorderdetail_pkey PRIMARY KEY (_id);


--
-- Name: api_task api_task_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_task
    ADD CONSTRAINT api_task_pkey PRIMARY KEY (_id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: api_classroom__class_code_id_dfa6be31; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_classroom__class_code_id_dfa6be31 ON public.api_classroom USING btree (_class_code_id);


--
-- Name: api_dish__name_id_d14ff1ae; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_dish__name_id_d14ff1ae ON public.api_dish USING btree (_name_id);


--
-- Name: api_dish__type_id_6f008052; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_dish__type_id_6f008052 ON public.api_dish USING btree (_type_id);


--
-- Name: api_dish__type_id_6f008052_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_dish__type_id_6f008052_like ON public.api_dish USING btree (_type_id varchar_pattern_ops);


--
-- Name: api_dishtype__id_e6b4cc43_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_dishtype__id_e6b4cc43_like ON public.api_dishtype USING btree (_id varchar_pattern_ops);


--
-- Name: api_feedback__accesible_element_id_e1e52b73; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_feedback__accesible_element_id_e1e52b73 ON public.api_feedback USING btree (_feedback_id);


--
-- Name: api_kitchenorder__id_id_464f9985; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_kitchenorder__id_id_464f9985 ON public.api_kitchenorder USING btree (_id_id);


--
-- Name: api_kitchenorderdetail__classroom_id_d2dcb091; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_kitchenorderdetail__classroom_id_d2dcb091 ON public.api_kitchenorderdetail USING btree (_classroom_id);


--
-- Name: api_kitchenorderdetail__dish_id_6f5e492d; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_kitchenorderdetail__dish_id_6f5e492d ON public.api_kitchenorderdetail USING btree (_dish_id);


--
-- Name: api_kitchenorderdetail__kitchen_order_id_a7564a31; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_kitchenorderdetail__kitchen_order_id_a7564a31 ON public.api_kitchenorderdetail USING btree (_kitchen_order_id);


--
-- Name: api_task__feedback_id_f968e681; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_task__feedback_id_f968e681 ON public.api_task USING btree (_feedback_id);


--
-- Name: api_task__name_id_2409c745; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX api_task__name_id_2409c745 ON public.api_task USING btree (_name_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: api_classroom api_classroom__class_code_id_dfa6be31_fk_api_acces; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_classroom
    ADD CONSTRAINT api_classroom__class_code_id_dfa6be31_fk_api_acces FOREIGN KEY (_class_code_id) REFERENCES public.api_accessibleelement(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_dish api_dish__name_id_d14ff1ae_fk_api_accessibleelement__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_dish
    ADD CONSTRAINT api_dish__name_id_d14ff1ae_fk_api_accessibleelement__id FOREIGN KEY (_name_id) REFERENCES public.api_accessibleelement(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_dish api_dish__type_id_6f008052_fk_api_dishtype__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_dish
    ADD CONSTRAINT api_dish__type_id_6f008052_fk_api_dishtype__id FOREIGN KEY (_type_id) REFERENCES public.api_dishtype(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_feedback api_feedback__feedback_id_d4cc5be6_fk_api_accessibleelement__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_feedback
    ADD CONSTRAINT api_feedback__feedback_id_d4cc5be6_fk_api_accessibleelement__id FOREIGN KEY (_feedback_id) REFERENCES public.api_accessibleelement(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_kitchenorder api_kitchenorder__id_id_464f9985_fk_api_task__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_kitchenorder
    ADD CONSTRAINT api_kitchenorder__id_id_464f9985_fk_api_task__id FOREIGN KEY (_id_id) REFERENCES public.api_task(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_kitchenorderdetail api_kitchenorderdeta__classroom_id_d2dcb091_fk_api_class; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_kitchenorderdetail
    ADD CONSTRAINT api_kitchenorderdeta__classroom_id_d2dcb091_fk_api_class FOREIGN KEY (_classroom_id) REFERENCES public.api_classroom(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_kitchenorderdetail api_kitchenorderdeta__kitchen_order_id_a7564a31_fk_api_kitch; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_kitchenorderdetail
    ADD CONSTRAINT api_kitchenorderdeta__kitchen_order_id_a7564a31_fk_api_kitch FOREIGN KEY (_kitchen_order_id) REFERENCES public.api_kitchenorder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_kitchenorderdetail api_kitchenorderdetail__dish_id_6f5e492d_fk_api_dish__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_kitchenorderdetail
    ADD CONSTRAINT api_kitchenorderdetail__dish_id_6f5e492d_fk_api_dish__id FOREIGN KEY (_dish_id) REFERENCES public.api_dish(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_task api_task__feedback_id_f968e681_fk_api_feedback__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_task
    ADD CONSTRAINT api_task__feedback_id_f968e681_fk_api_feedback__id FOREIGN KEY (_feedback_id) REFERENCES public.api_feedback(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_task api_task__name_id_2409c745_fk_api_accessibleelement__id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.api_task
    ADD CONSTRAINT api_task__name_id_2409c745_fk_api_accessibleelement__id FOREIGN KEY (_name_id) REFERENCES public.api_accessibleelement(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

