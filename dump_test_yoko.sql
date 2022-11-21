--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE post_db;




--
-- Drop roles
--

DROP ROLE postgres;


--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:XfMgkOiV45hQwIydX1nv4g==$cfIyOQtOjEfBTQChaZi+0y8QgPa61erqc5P7KMXIzdg=:D2D+ejVlOreL5R32bB7VRQPd6+exYp+SLbuyY3nXZgI=';

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0 (Debian 15.0-1.pgdg110+1)
-- Dumped by pg_dump version 15.0 (Debian 15.0-1.pgdg110+1)

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

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO postgres;

\connect template1

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

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: postgres
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

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

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: postgres
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "post_db" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0 (Debian 15.0-1.pgdg110+1)
-- Dumped by pg_dump version 15.0 (Debian 15.0-1.pgdg110+1)

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

--
-- Name: post_db; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE post_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE post_db OWNER TO postgres;

\connect post_db

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id integer NOT NULL,
    name character varying(255),
    phone_number character varying(255),
    shop_id integer NOT NULL
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: customer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customer_id_seq OWNER TO postgres;

--
-- Name: customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.customer_id_seq OWNED BY public.customer.id;


--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    id integer NOT NULL,
    name character varying(255),
    phone_number character varying(255),
    shop_id integer NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: employee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employee_id_seq OWNER TO postgres;

--
-- Name: employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.employee_id_seq OWNED BY public.employee.id;


--
-- Name: order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."order" (
    id integer NOT NULL,
    status character varying(255),
    shop_id integer NOT NULL,
    author_id integer NOT NULL,
    executor_id integer NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    expiration_data timestamp with time zone
);


ALTER TABLE public."order" OWNER TO postgres;

--
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_id_seq OWNER TO postgres;

--
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_id_seq OWNED BY public."order".id;


--
-- Name: shop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shop (
    id integer NOT NULL,
    title character varying
);


ALTER TABLE public.shop OWNER TO postgres;

--
-- Name: shop_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shop_id_seq OWNER TO postgres;

--
-- Name: shop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shop_id_seq OWNED BY public.shop.id;


--
-- Name: visit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.visit (
    id integer NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    executor_id integer NOT NULL,
    author_id integer NOT NULL,
    shop_id integer NOT NULL,
    order_id integer
);


ALTER TABLE public.visit OWNER TO postgres;

--
-- Name: visit_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.visit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.visit_id_seq OWNER TO postgres;

--
-- Name: visit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.visit_id_seq OWNED BY public.visit.id;


--
-- Name: customer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer ALTER COLUMN id SET DEFAULT nextval('public.customer_id_seq'::regclass);


--
-- Name: employee id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee ALTER COLUMN id SET DEFAULT nextval('public.employee_id_seq'::regclass);


--
-- Name: order id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order" ALTER COLUMN id SET DEFAULT nextval('public.order_id_seq'::regclass);


--
-- Name: shop id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shop ALTER COLUMN id SET DEFAULT nextval('public.shop_id_seq'::regclass);


--
-- Name: visit id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit ALTER COLUMN id SET DEFAULT nextval('public.visit_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
70a746d08fd1
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (id, name, phone_number, shop_id) FROM stdin;
84	ultricies	7771	1
85	iaculis	7772	1
86	magna	7773	2
87	eu	7774	2
88	commodo	7775	3
89	Pellentesque	7776	3
90	habitant	7777	4
91	morbi	7778	4
92	tristique	7779	5
93	senectus	77710	5
94	et	77711	6
95	malesuada	77712	6
96	fames	77713	7
97	ac	77714	7
98	turpis	77715	8
99	egestas	77716	8
100	Mauris	77717	9
101	ac	77718	9
102	dolor	77719	10
103	nec	77720	10
104	risus	77721	11
105	efficitur	77722	11
106	tempus	77723	12
107	consectetur	77724	13
108	sem	77725	13
109	Phasellus	77726	14
110	vehicula	77727	14
111	amet	77728	15
112	neque	77729	15
113	faucibus	77730	16
114	amet	77731	16
115	mollis	77732	17
116	velit	77733	17
117	mollis	77734	17
118	Praesent	77735	18
119	dignissim	77736	18
120	dictum	77737	19
121	Maecenas	77738	19
122	orci	77739	20
123	laoreet	77740	20
124	ultricies	77741	21
125	felis	77742	21
126	lectus	77743	22
127	auctor	77744	22
128	sem	77745	23
129	placerat	77746	23
130	viverra	77747	24
131	amet	77748	24
132	pulvinar	77749	25
133	ligula	77750	25
134	elementum	77751	26
135	Pellentesque	77752	26
136	nibh	77753	27
137	interdum	77754	27
138	pharetra	77755	28
139	orci	77756	28
140	egestas	77757	29
141	velit	77758	30
142	Proin	77759	30
143	mattis	77760	31
144	justo	77761	31
145	arcu	77762	32
146	venenatis	77763	32
147	Nulla	77764	33
148	placerat	77765	33
149	posuere	77766	34
150	leo	77767	34
151	eget	77768	34
152	ultricies	77769	34
153	enim	77770	35
154	bibendum	77771	35
155	non	77772	35
156	Phasellus	77773	36
157	massa	77774	37
158	erat	77775	38
159	ultrices	77776	39
160	nec	77777	40
161	purus	77778	41
162	ut	77779	42
163	auctor	77780	43
164	risus	77781	44
165	Donec	77782	44
166	arcu	77783	45
167	mauris	77784	45
168	Neque	77785	46
169	porro	77786	46
170	quisquam	77787	47
171	qui	77788	47
172	dolorem	77789	48
173	ipsum	77790	48
174	quia	77791	49
175	dolor	77792	49
176	amet	77793	50
177	consectetur	77794	51
178	adipisci	77795	52
179	velit	77796	52
180	gravida	77797	53
181	auctor	77798	53
182	Vivamus	77799	54
183	Aenean	777100	54
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (id, name, phone_number, shop_id) FROM stdin;
1	Orci	7771	1
3	varius	7772	1
4	natoque	7773	2
6	penatibus	7774	2
7	et	7775	3
8	magnis	7776	3
9	dis	7777	3
10	parturient	7778	4
11	montes	7779	5
12	nascetur	77710	6
13	ridiculus	77711	6
14	mus	77712	6
15	Aliquam	77713	7
16	erat	77714	8
17	volutpat	77715	8
18	Ut	77716	9
19	lacinia	77717	9
20	vitae	77718	10
21	ex	77719	10
22	iaculis	77720	10
23	fermentum	77721	10
24	Ut	77722	11
25	consectetur	77723	11
26	cursus	77724	12
28	ante	77725	12
29	ante	77726	13
30	ac	77727	13
31	commodo	77728	14
32	Donec	77729	14
33	sit	77730	15
34	amet	77731	15
35	magna	77732	16
36	risus	77733	16
37	Aenean	77734	17
38	venenatis	77735	17
39	faucibus	77736	17
40	sapien	77737	18
41	Phasellus	77738	18
42	dignissim	77739	19
43	enim	77740	20
44	libero	77741	20
45	eu	77742	21
46	laoreet	77743	21
47	diam	77744	22
48	vestibulum	77745	22
49	gravida	77746	23
50	Vivamus	77747	23
51	nec	77748	24
52	felis	77749	24
53	lobortis	77750	25
54	volutpat	77751	25
55	purus	77752	26
56	tincidunt	77753	26
57	efficitur	77754	27
58	ligula	77755	27
59	Nullam	77756	28
60	vitae	77757	28
61	erat	77758	29
62	sit	77759	29
63	amet	77760	30
64	ligula	77761	30
65	iaculis	77762	31
66	pulvinar	77763	31
67	Aliquam	77764	32
68	ultricies	77765	32
69	enim	77766	33
70	enim	77767	32
71	nunc	77768	33
72	accumsan	77769	33
73	id	77770	34
74	condimentum	77771	35
75	eros	77772	35
76	bibendum	77773	36
77	Phasellus	77774	37
78	Nullam	77775	38
79	maximus	77776	39
80	sem	77777	40
81	eu	77778	41
82	quis	77779	42
83	enim	77780	43
84	molestie	77781	44
85	molestie	77782	44
86	Etiam	77783	45
87	mollis	77784	45
88	augue	77785	46
89	et	77786	46
90	commodo	77787	47
91	dolor	77788	47
92	scelerisque	77789	48
93	in	77790	48
94	Aliquam	77791	49
95	ac	77792	49
96	diam	77793	50
97	dapibus	77794	51
98	laoreet	77795	52
99	velit	77796	52
100	quis	77797	53
101	auctor	77798	53
102	tortor	77799	54
103	Integer	777100	54
\.


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."order" (id, status, shop_id, author_id, executor_id, created_at, expiration_data) FROM stdin;
1	started	1	84	1	2022-11-21 12:12:08.404571+00	2022-11-21 12:12:08.404597+00
2	started	1	84	3	2022-11-21 12:12:08.404571+00	2022-11-21 12:12:08.404597+00
3	started	1	85	1	2022-11-21 12:12:08.404571+00	2022-11-21 12:12:08.404597+00
4	started	2	86	4	2022-11-21 14:34:11.824372+00	2022-11-21 14:34:11.824459+00
5	started	2	87	4	2022-11-21 14:34:11.824372+00	2022-11-21 14:34:11.824459+00
6	started	3	88	7	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
7	started	3	89	8	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
8	started	4	90	10	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
9	started	4	91	10	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
10	started	5	92	11	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
11	started	5	93	11	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
12	started	6	94	12	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
13	started	6	95	13	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
14	started	6	95	13	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
15	started	7	96	15	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
16	started	7	97	15	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
17	started	8	98	16	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
18	started	8	99	17	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
19	started	9	100	18	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
20	started	9	101	19	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
21	started	10	102	20	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
22	started	10	103	21	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
23	started	10	103	22	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
24	started	11	104	24	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
25	started	11	105	25	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
26	started	12	106	26	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
27	started	12	106	28	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
28	started	13	107	29	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
29	started	13	108	30	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
30	started	14	109	31	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
31	started	14	110	32	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
32	started	15	111	33	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
33	started	15	111	34	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
34	started	16	113	35	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
35	started	16	113	36	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
36	started	16	113	36	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
37	started	17	115	37	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
38	started	17	116	38	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
39	started	17	116	39	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
40	started	18	118	40	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
41	started	18	119	41	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
42	started	19	121	42	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
43	started	19	121	42	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
44	started	20	122	43	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
45	started	20	123	44	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
46	started	20	123	44	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
47	started	21	124	45	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
48	started	21	125	46	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
49	started	22	126	47	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
50	started	22	127	48	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
51	started	23	128	49	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
52	started	23	129	50	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
53	started	23	129	50	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
54	started	24	130	51	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
55	started	24	131	52	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
56	started	25	132	53	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
57	started	25	133	54	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
58	started	26	134	55	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
59	started	26	135	56	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
60	started	27	136	57	2022-11-21 14:34:11.824372+00	2022-11-22 00:00:00+00
61	started	27	137	58	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
62	started	28	138	59	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
63	started	28	139	60	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
64	started	29	140	61	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
65	started	29	140	62	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
66	started	30	141	63	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
67	started	30	142	64	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
68	started	31	143	65	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
69	started	31	144	66	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
70	started	32	145	68	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
71	started	32	145	70	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
72	started	33	147	71	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
73	started	33	148	72	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
74	started	33	148	69	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
75	started	34	149	73	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
76	started	34	150	73	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
77	started	34	151	73	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
78	started	34	152	73	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
79	started	35	153	74	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
80	started	35	154	75	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
81	started	35	155	75	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
82	started	36	156	76	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
83	started	37	157	77	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
84	started	37	157	77	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
85	started	38	158	78	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
86	started	38	158	78	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
87	started	39	159	79	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
88	started	39	159	79	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
89	started	39	159	79	2022-11-21 14:34:11.848673+00	2022-11-20 00:00:00+00
90	started	40	160	80	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
91	started	40	160	80	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
92	started	40	160	80	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
93	started	40	160	80	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
94	started	40	160	80	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
95	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
96	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
97	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
98	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
99	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
100	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
101	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
102	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
103	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
104	started	41	161	81	2022-11-21 14:34:11.848673+00	2022-11-22 00:00:00+00
105	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
106	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
107	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
108	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
109	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
110	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
111	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
112	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
113	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
114	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
115	started	42	162	82	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
116	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
117	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
118	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
119	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
120	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
121	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
122	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
123	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
124	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
125	started	43	163	83	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
126	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
127	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
128	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
129	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
130	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
131	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
132	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
133	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
134	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
135	started	44	164	84	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
136	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
137	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
138	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
139	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
140	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
141	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
142	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
143	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
144	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
145	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
146	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
147	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
148	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
149	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
150	started	44	165	85	2022-11-21 14:34:11.848673+00	2022-11-21 00:00:00+00
151	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
152	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
153	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
154	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
155	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
156	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
157	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
158	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
159	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
160	ended	45	166	86	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
161	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
162	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
163	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
164	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
165	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
166	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
167	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
168	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
169	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
170	ended	45	167	87	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
171	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
172	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
173	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
174	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
175	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
176	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
177	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
178	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
179	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
180	awaiting	46	168	88	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
181	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
182	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
183	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
184	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
185	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
186	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
187	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
188	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
189	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
190	awaiting	46	169	89	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
191	awaiting	47	170	90	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
192	awaiting	47	171	91	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
193	awaiting	47	171	91	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
194	awaiting	48	172	92	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
195	awaiting	48	172	92	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
196	awaiting	48	173	93	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
197	awaiting	48	173	93	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
198	awaiting	49	174	94	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
199	awaiting	49	175	95	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
200	awaiting	49	175	95	2022-11-21 14:34:11.848673+00	2022-11-19 00:00:00+00
\.


--
-- Data for Name: shop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shop (id, title) FROM stdin;
1	Adidas
2	Lorem
3	ipsum
4	dolor
5	sit
6	amet
7	consectetur
8	adipiscing
9	elit
10	Donec
11	non
12	tristique
13	velit
14	Pellentesque
15	arcu
16	arcu
17	eleifend
18	eleifend
19	efficitur
20	non
21	pulvinar
22	non
23	erat
24	Morbi
25	purus
26	lorem
27	laoreet
28	ac
29	interdum
30	at
31	sollicitudin
32	quis
33	augue
34	Nulla
35	nisl
36	lacus
37	fringilla
38	eu
39	interdum
40	vel
41	efficitur
42	sed
43	dolor
44	Orci
45	varius
46	natoque
47	penatibus
48	et
49	magnis
50	dis
51	parturient
52	montes
53	nascetur
54	ridiculus
55	mus
56	Praesent
57	laoreet
58	urna
59	et
60	sollicitudin
61	egestas
62	Cras
63	sed
64	mauris
65	nisl
66	Cras
67	rhoncus
68	massa
69	ante
70	sit
71	amet
72	molestie
73	quam
74	vulputate
75	vel
76	Duis
77	eget
78	maximus
79	justo
80	sed
81	aliquet
82	libero
83	Praesent
84	quis
85	augue
86	ut
87	quam
88	tempor
89	convallis
90	Praesent
91	egestas
92	lacinia
93	est
94	quis
95	cursus
96	Phasellus
97	elit
98	magna
99	vulputate
100	augue
\.


--
-- Data for Name: visit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.visit (id, created_at, executor_id, author_id, shop_id, order_id) FROM stdin;
1	2022-11-21 00:00:00+00	7	88	3	6
2	2022-11-21 00:00:00+00	8	89	3	7
3	2022-11-21 15:33:53.526582+00	10	90	4	8
4	2022-11-21 15:33:53.526582+00	10	91	4	9
5	2022-11-21 15:33:53.526582+00	11	92	5	10
6	2022-11-21 15:33:53.526582+00	11	93	5	11
7	2022-11-21 15:33:53.526582+00	12	94	6	12
8	2022-11-21 15:33:53.526582+00	13	95	6	13
9	2022-11-21 15:33:53.526582+00	13	95	6	14
10	2022-11-21 15:33:53.526582+00	15	96	7	15
11	2022-11-21 15:33:53.526582+00	15	96	7	16
12	2022-11-21 15:33:53.526582+00	16	98	8	17
13	2022-11-21 15:33:53.526582+00	17	99	8	18
14	2022-11-21 15:33:53.526582+00	18	100	9	19
15	2022-11-21 15:33:53.526582+00	19	101	9	20
16	2022-11-21 15:33:53.526582+00	20	102	10	21
17	2022-11-21 15:33:53.526582+00	21	103	10	22
18	2022-11-21 15:33:53.526582+00	22	103	10	23
19	2022-11-21 15:33:53.526582+00	24	104	11	24
20	2022-11-21 15:33:53.526582+00	25	105	11	25
21	2022-11-21 15:33:53.526582+00	26	106	12	26
22	2022-11-21 15:33:53.526582+00	28	106	12	27
23	2022-11-21 15:33:53.526582+00	29	107	13	28
24	2022-11-21 15:33:53.526582+00	30	108	13	29
25	2022-11-21 15:33:53.526582+00	31	109	14	30
26	2022-11-21 15:33:53.526582+00	32	110	14	31
27	2022-11-21 15:33:53.526582+00	33	111	15	32
28	2022-11-21 15:33:53.526582+00	34	111	15	33
29	2022-11-21 15:33:53.526582+00	35	113	16	34
30	2022-11-21 15:33:53.526582+00	36	113	16	35
31	2022-11-21 15:33:53.526582+00	36	113	16	36
32	2022-11-21 15:33:53.805727+00	80	160	40	90
33	2022-11-21 15:33:53.805727+00	80	160	40	91
34	2022-11-21 15:33:53.805727+00	80	160	40	92
35	2022-11-21 15:33:53.805727+00	80	160	40	93
36	2022-11-21 15:33:53.805727+00	80	160	40	94
37	2022-11-21 15:33:53.805727+00	81	161	41	95
38	2022-11-21 15:33:53.805727+00	81	161	41	96
39	2022-11-21 15:33:53.805727+00	81	161	41	97
40	2022-11-21 15:33:53.805727+00	81	161	41	98
41	2022-11-21 15:33:53.805727+00	81	161	41	99
42	2022-11-21 15:33:53.805727+00	81	161	41	100
43	2022-11-21 15:33:53.805727+00	81	161	41	101
44	2022-11-21 15:33:53.805727+00	81	161	41	102
45	2022-11-21 15:33:53.805727+00	81	161	41	103
46	2022-11-21 15:33:53.805727+00	81	161	41	104
47	2022-11-20 00:00:00+00	82	162	42	105
48	2022-11-20 00:00:00+00	82	162	42	106
49	2022-11-20 00:00:00+00	82	162	42	107
50	2022-11-20 00:00:00+00	82	162	42	108
51	2022-11-20 00:00:00+00	82	162	42	109
52	2022-11-20 00:00:00+00	82	162	42	110
53	2022-11-20 00:00:00+00	82	162	42	111
54	2022-11-20 00:00:00+00	82	162	42	112
55	2022-11-20 00:00:00+00	82	162	42	113
56	2022-11-20 00:00:00+00	82	162	42	114
57	2022-11-20 00:00:00+00	82	162	42	115
58	2022-11-20 00:00:00+00	83	163	43	116
59	2022-11-20 00:00:00+00	83	163	43	117
60	2022-11-20 00:00:00+00	83	163	43	118
61	2022-11-20 00:00:00+00	83	163	43	119
62	2022-11-20 00:00:00+00	83	163	43	120
63	2022-11-20 00:00:00+00	83	163	43	121
64	2022-11-20 00:00:00+00	83	163	43	122
65	2022-11-20 00:00:00+00	83	163	43	123
66	2022-11-20 00:00:00+00	83	163	43	124
67	2022-11-20 00:00:00+00	83	163	43	125
68	2022-11-20 00:00:00+00	84	164	44	126
69	2022-11-20 00:00:00+00	84	164	44	127
70	2022-11-20 00:00:00+00	84	164	44	128
71	2022-11-20 00:00:00+00	84	164	44	129
72	2022-11-20 00:00:00+00	84	164	44	130
73	2022-11-20 00:00:00+00	84	164	44	131
74	2022-11-20 00:00:00+00	84	164	44	132
75	2022-11-20 00:00:00+00	84	164	44	133
76	2022-11-20 00:00:00+00	84	164	44	134
77	2022-11-20 00:00:00+00	84	164	44	135
78	2022-11-20 00:00:00+00	85	165	44	136
79	2022-11-20 00:00:00+00	85	165	44	137
80	2022-11-20 00:00:00+00	85	165	44	138
81	2022-11-20 00:00:00+00	85	165	44	139
82	2022-11-20 00:00:00+00	85	165	44	140
83	2022-11-20 00:00:00+00	85	165	44	141
84	2022-11-20 00:00:00+00	85	165	44	142
85	2022-11-20 00:00:00+00	85	165	44	143
86	2022-11-20 00:00:00+00	85	165	44	144
87	2022-11-20 00:00:00+00	85	165	44	145
88	2022-11-20 00:00:00+00	85	165	44	146
89	2022-11-20 00:00:00+00	85	165	44	147
90	2022-11-20 00:00:00+00	85	165	44	148
91	2022-11-20 00:00:00+00	85	165	44	149
92	2022-11-19 00:00:00+00	86	166	45	151
93	2022-11-19 00:00:00+00	86	166	45	152
94	2022-11-19 00:00:00+00	86	166	45	153
95	2022-11-19 00:00:00+00	86	166	45	154
96	2022-11-19 00:00:00+00	86	166	45	155
97	2022-11-19 00:00:00+00	86	166	45	156
98	2022-11-19 00:00:00+00	86	166	45	157
99	2022-11-19 00:00:00+00	86	166	45	158
100	2022-11-19 00:00:00+00	86	166	45	159
101	2022-11-19 00:00:00+00	86	166	45	160
\.


--
-- Name: customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_id_seq', 183, true);


--
-- Name: employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employee_id_seq', 105, true);


--
-- Name: order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_id_seq', 200, true);


--
-- Name: shop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shop_id_seq', 100, true);


--
-- Name: visit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.visit_id_seq', 101, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: customer customer_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_phone_number_key UNIQUE (phone_number);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: employee employee_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_phone_number_key UNIQUE (phone_number);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (id);


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- Name: shop shop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shop
    ADD CONSTRAINT shop_pkey PRIMARY KEY (id);


--
-- Name: visit visit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_pkey PRIMARY KEY (id);


--
-- Name: customer customer_shop_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_shop_id_fkey FOREIGN KEY (shop_id) REFERENCES public.shop(id);


--
-- Name: employee employee_shop_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_shop_id_fkey FOREIGN KEY (shop_id) REFERENCES public.shop(id);


--
-- Name: order order_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.customer(id);


--
-- Name: order order_executor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_executor_id_fkey FOREIGN KEY (executor_id) REFERENCES public.employee(id);


--
-- Name: order order_shop_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_shop_id_fkey FOREIGN KEY (shop_id) REFERENCES public.shop(id);


--
-- Name: visit visit_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.customer(id);


--
-- Name: visit visit_executor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_executor_id_fkey FOREIGN KEY (executor_id) REFERENCES public.employee(id);


--
-- Name: visit visit_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_order_id_fkey FOREIGN KEY (order_id) REFERENCES public."order"(id);


--
-- Name: visit visit_shop_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_shop_id_fkey FOREIGN KEY (shop_id) REFERENCES public.shop(id);


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0 (Debian 15.0-1.pgdg110+1)
-- Dumped by pg_dump version 15.0 (Debian 15.0-1.pgdg110+1)

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

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

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

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

